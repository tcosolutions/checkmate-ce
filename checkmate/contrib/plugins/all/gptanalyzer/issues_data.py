issues_data = {
    'CodeInjection': {
        'categories': ['Injection'],
        'description': 'Code injection occurs when an attacker is able to insert or inject malicious code into an application.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Code Injection'
    },
    'SQLInjection': {
        'categories': ['Injection'],
        'description': 'SQL injection occurs when an attacker is able to manipulate a query to execute malicious SQL code.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'SQL Injection'
    },
    'OSCommandInjection': {
        'categories': ['Injection'],
        'description': 'OS command injection allows an attacker to execute arbitrary OS commands on the server.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'OS Command Injection'
    },
    'CrossSiteScriptingXSS': {
        'categories': ['Scripting'],
        'description': 'Cross-Site Scripting (XSS) occurs when an attacker injects malicious scripts into a web page.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Cross-Site Scripting (XSS)'
    },
    'InsecureDeserialization': {
        'categories': ['Deserialization'],
        'description': 'Insecure deserialization occurs when untrusted data is deserialized and executed, leading to remote code execution or other attacks.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Insecure Deserialization'
    },
    'CrossSiteRequestForgeryCSRF': {
        'categories': ['Forgery'],
        'description': 'Cross-Site Request Forgery (CSRF) forces a logged-in user to perform unwanted actions on a web application.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Cross-Site Request Forgery (CSRF)'
    },
    'SensitiveDataExposure': {
        'categories': ['DataExposure'],
        'description': 'Sensitive data exposure occurs when sensitive data like passwords or credit card numbers are exposed in an unprotected manner.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Sensitive Data Exposure'
    },
    'BrokenAuthentication': {
        'categories': ['Authentication'],
        'description': 'Broken authentication occurs when attackers are able to gain unauthorized access to accounts or services.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Broken Authentication'
    },
    'BrokenAccessControl': {
        'categories': ['AccessControl'],
        'description': 'Broken access control occurs when a user is able to access resources or perform actions they should not be allowed to.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Broken Access Control'
    },
    'SecurityMisconfiguration': {
        'categories': ['Misconfiguration'],
        'description': 'Security misconfiguration occurs when a system is set up insecurely, allowing for possible exploitation.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Security Misconfiguration'
    },
    'UsingComponentsWithKnownVulnerabilities': {
        'categories': ['Components'],
        'description': 'Using components with known vulnerabilities exposes the system to known exploits.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Using Components with Known Vulnerabilities'
    },
    'XMLExternalEntityXXEInjection': {
        'categories': ['Injection'],
        'description': 'XML External Entity (XXE) injection allows an attacker to interfere with XML processing and extract data.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'XML External Entity (XXE) Injection'
    },
    'BrokenCryptography': {
        'categories': ['Cryptography'],
        'description': 'Broken cryptography occurs when weak or outdated cryptographic algorithms are used, compromising data integrity.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Broken Cryptography'
    },
    'InsufficientLoggingMonitoring': {
        'categories': ['Logging'],
        'description': 'Insufficient logging and monitoring allows attackers to perform actions without detection.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 3,
        'title': 'Insufficient Logging & Monitoring'
    },
    'ImproperErrorHandling': {
        'categories': ['ErrorHandling'],
        'description': 'Improper error handling may expose sensitive information about the system to attackers.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 3,
        'title': 'Improper Error Handling'
    },
    'BufferOverflow': {
        'categories': ['Overflow'],
        'description': 'Buffer overflow occurs when data overflows into adjacent memory, potentially leading to arbitrary code execution.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Buffer Overflow'
    },
    'PathTraversal': {
        'categories': ['Traversal'],
        'description': 'Path traversal allows attackers to access files and directories that are stored outside the web root folder.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Path Traversal'
    },
    'InsecureDirectObjectReferencesIDOR': {
        'categories': ['ObjectReferences'],
        'description': 'Insecure Direct Object References (IDOR) allow attackers to bypass access control checks by manipulating object identifiers.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Insecure Direct Object References (IDOR)'
    },
    'LackOfDataProtection': {
        'categories': ['DataProtection'],
        'description': 'Lack of data protection means failure to secure sensitive data during storage and transmission.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Lack of Data Protection'
    },
    'ServerSideRequestForgerySSRF': {
        'categories': ['RequestForgery'],
        'description': 'Server-Side Request Forgery (SSRF) allows an attacker to make requests from the server-side application to internal systems.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Server-Side Request Forgery (SSRF)'
    },
    'UntrustedInputValidation': {
        'categories': ['InputValidation'],
        'description': 'Untrusted input validation allows attackers to send malicious data, leading to potential exploits.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Untrusted Input Validation'
    },
    'RaceConditions': {
        'categories': ['Conditions'],
        'description': 'Race conditions occur when two processes attempt to change shared data simultaneously, leading to unexpected behavior.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Race Conditions'
    },
    'ImproperAuthorization': {
        'categories': ['Authorization'],
        'description': 'Improper authorization allows users to gain access to parts of the system they should not.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 1,
        'title': 'Improper Authorization'
    },
    'ImproperValidationOfRedirectsAndForwards': {
        'categories': ['RedirectValidation'],
        'description': 'Improper validation of redirects and forwards can be exploited to redirect users to malicious sites.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Improper Validation of Redirects and Forwards'
    },
    'InsufficientSecurityControls': {
        'categories': ['SecurityControls'],
        'description': 'Insufficient security controls fail to protect the system against known vulnerabilities and exploits.',
        'file': '%(issue.file)s',
        'line': '%(issue.line)s',
        'severity': 2,
        'title': 'Insufficient Security Controls'
    }
}

