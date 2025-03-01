ADMIN_PATHS = [
    'admin/',
    'administrator/',
    'admin.php',
    'admin.asp',
    'admin.aspx',
    'admin.jsp',
    'admin.html',
    'admin.cfm',
    'admin.py',
    'admin.rb',
    'wp-admin/',
    'wp-login.php',
    'wp-admin/admin-ajax.php',
    'wordpress/wp-admin',
    'wp/wp-admin',
    'blog/wp-admin'
]

ADMIN_EXTENSIONS = [
    '.php',
    '.html',
    '.asp',
    '.aspx',
    '.jsp',
    '.cfm',
    '.cgi',
    '.py',
    '.rb',
    '.pl',
    '.shtml',
    '.action'
]

# Generate additional combinations
GENERATED_PATHS = [f"{base}{ext}" for base in ADMIN_PATHS for ext in ADMIN_EXTENSIONS]

# Combine all paths
ALL_PATHS = list(set(ADMIN_PATHS + GENERATED_PATHS))
