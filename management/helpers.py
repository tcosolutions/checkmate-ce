from typing import Any, Dict, Optional
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import logging
from ..lib.models import Backend
from ..exceptions import ConfigurationError

logger = logging.getLogger(__name__)

def validate_config(config: Dict[str, Any]) -> None:
    """Validate the configuration dictionary.
    
    Args:
        config: Configuration dictionary to validate
        
    Raises:
        ConfigurationError: If configuration is invalid
    """
    required_fields = {
        'sql': ['host', 'database', 'user'],
        'sqlfile': []
    }
    
    backend_type = config.get('backend', {}).get('type', 'sql')
    if backend_type not in required_fields:
        raise ConfigurationError(f"Invalid backend type: {backend_type}")
        
    for field in required_fields[backend_type]:
        if not config.get('backend', {}).get(field):
            raise ConfigurationError(f"Missing required field: {field}")

def get_connection_string(config: Dict[str, Any]) -> str:
    """Generate database connection string from config.
    
    Args:
        config: Configuration dictionary
        
    Returns:
        str: Database connection string
        
    Raises:
        ConfigurationError: If connection string cannot be generated
    """
    try:
        backend = config.get('backend', {})
        template = "postgresql://{user}:{password}@{host}:{port}/{database}"
        return template.format(
            user=backend.get('user'),
            password=backend.get('password', ''),
            host=backend.get('host', 'localhost'),
            port=backend.get('port', 5432),
            database=backend.get('database')
        )
    except Exception as e:
        raise ConfigurationError(f"Failed to generate connection string: {str(e)}")

def get_backend(
    project_path: str,
    project_config: Dict[str, Any],
    settings: Optional[Dict[str, Any]] = None
) -> Backend:
    """Create and return appropriate backend based on project configuration.
    
    Args:
        project_path: Path to the project
        project_config: Project configuration dictionary
        settings: Optional additional settings
        
    Returns:
        Initialized Backend instance
        
    Raises:
        ConfigurationError: If configuration is invalid
        ConnectionError: If database connection fails
    """
    try:
        # Validate configuration
        validate_config(project_config)
        
        backend_type = project_config.get('backend', {}).get('type', 'sql')
        pool_size = settings.get('pool_size', 5) if settings else 5
        
        logger.info(f"Initializing {backend_type} backend")
        
        if backend_type == 'sql':
            connection_string = get_connection_string(project_config)
            engine = create_engine(
                connection_string,
                poolclass=QueuePool,
                pool_size=pool_size,
                max_overflow=10,
                pool_timeout=30
            )
        elif backend_type == 'sqlfile':
            if not project_path:
                raise ConfigurationError("Project path is required for sqlfile backend")
            engine = project_path
        else:
            raise ConfigurationError(f"Unknown backend type: {backend_type}")
        
        backend = Backend(engine, backend_type, pool_size)
        
        # Test connection
        backend.test_connection()
        
        return backend
        
    except Exception as e:
        logger.error(f"Backend initialization failed: {str(e)}")
        raise 