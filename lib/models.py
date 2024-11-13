from blitzdb import Document
from blitzdb.backends.sql.backend import Backend as FileBackend
from typing import Any, Optional, Dict
import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)

class Backend(FileBackend):
    def __init__(self, engine: Any, backend_type: str = 'sql', pool_size: int = 5) -> None:
        """Initialize BlitzDB backend with specified engine and type.
        
        Args:
            engine: SQL connection engine or file path depending on backend_type
            backend_type: Type of backend ('sql' or 'sqlfile')
            pool_size: Connection pool size for SQL backend
            
        Raises:
            ValueError: If backend_type is not supported
        """
        if backend_type not in ['sql', 'sqlfile']:
            raise ValueError(f"Unsupported backend type: {backend_type}")
            
        self.backend_type = backend_type
        self.engine = engine
        self.pool_size = pool_size
        
        backend_params = {
            'sql': {
                'connection': engine,
                'backend': 'sql',
                'pool_size': pool_size
            },
            'sqlfile': {
                'path': engine,
                'backend': 'sqlfile'
            }
        }.get(backend_type)
        
        logger.debug(f"Initializing {backend_type} backend with params: {backend_params}")
        super().__init__(**backend_params)

    def test_connection(self) -> bool:
        """Test the backend connection.
        
        Returns:
            bool: True if connection is successful
            
        Raises:
            ConnectionError: If connection test fails
        """
        try:
            if self.backend_type == 'sql':
                with self.engine.connect() as conn:
                    conn.execute('SELECT 1')
            elif self.backend_type == 'sqlfile':
                # Test file access
                with open(self.engine, 'a+') as _:
                    pass
            logger.info(f"Connection test successful for {self.backend_type} backend")
            return True
        except Exception as e:
            logger.error(f"Connection test failed: {str(e)}")
            raise ConnectionError(f"Connection test failed: {str(e)}")

    @contextmanager
    def session(self):
        """Context manager for database sessions.
        
        Yields:
            Backend: Self with active session
            
        Example:
            with backend.session() as session:
                session.save(document)
        """
        try:
            yield self
            self.commit()
        except Exception as e:
            logger.error(f"Session error: {str(e)}")
            self.rollback()
            raise
        finally:
            if self.backend_type == 'sql':
                self.engine.dispose()

    def close(self) -> None:
        """Properly close backend connections."""
        try:
            if self.backend_type == 'sql':
                self.engine.dispose()
            logger.info(f"Closed {self.backend_type} backend connection")
        except Exception as e:
            logger.error(f"Error closing backend: {str(e)}")
            raise 
