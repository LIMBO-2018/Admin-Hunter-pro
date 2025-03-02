ADMIN_PATHS = [
    # Common Admin Paths
    'admin/',
    'administrator/',
    'admincp/',
    'admins/',
    'admin/login/',
    'admin/login.php',
    'admin/cp.php',
    'admin/dashboard/',
    'admin_area/',
    'admin-login/',
    'adminpanel/',
    'admincontrol/',
    'adm/',
    'moderator/',
    'webadmin/',
    'useradmin/',
    'sysadmin/',
    'manage/',
    'management/',
    'control/',
    'cp/',
    'cpanel/',
    'panel/',

    # WordPress
    'wp-admin/',
    'wp-login/',
    'wp-login.php',
    'wordpress/wp-admin/',
    'wp/wp-admin/',
    'blog/wp-admin/',

    # Joomla
    'administrator/',
    'joomla/administrator/',
    'cms/administrator/',

    # Drupal
    'user/login/',
    'user/admin/',
    'user/',
    'admin/user/',

    # Magento
    'admin_xxxxx/',
    'magento_admin/',
    'index.php/admin/',

    # PrestaShop
    'adminpanel/',
    'admin123/',
    'admin_secure/',

    # OpenCart
    'admin/index.php',
    'administration/index.php',

    # Custom Paths
    'backend/',
    'control-panel/',
    'member/',
    'members/',
    'memberadmin/',
    'site-admin/',
    'site_admin/',
    'administratorlogin/',
    'auth/',
    'auth/login/',
    'signin/',
    'login/',
    'logon/',
    'manager/',
    'portal/',
    'supervisor/',
    'moderator/',
    'customer/',
    'customers/',
    'staff/',
    'console/',
    'access/',
    'secure/',
    'security/',
]

ADMIN_EXTENSIONS = [
    '.php',
    '.html',
    '.htm',
    '.asp',
    '.aspx',
    '.jsp',
    '.jspx',
    '.do',
    '.action',
    '.cfm',
    '.cgi',
    '.pl',
    '.py',
    '.rb',
    '.shtml',
    '.xml',
    '.json',
    '',  # For paths without extensions
]

# Language-specific admin paths
LOCALIZED_PATHS = [
    'admin-de/',    # German
    'admin-fr/',    # French
    'admin-es/',    # Spanish
    'admin-ru/',    # Russian
    'admin-ar/',    # Arabic
    'admin-cn/',    # Chinese
    'admin-jp/',    # Japanese
    'admin-kr/',    # Korean
    'yonetim/',     # Turkish
    'administrador/', # Portuguese/Spanish
    'beheerder/',   # Dutch
]

# E-commerce Platforms
ECOMMERCE_PATHS = [
    'shop/admin/',
    'shopping/admin/',
    'store/admin/',
    'store-admin/',
    'merchant/',
    'merchants/',
    'vendor/',
    'vendors/',
    'seller/',
    'sellers/',
]

# Generate combinations
GENERATED_PATHS = [f"{base}{ext}" for base in ADMIN_PATHS for ext in ADMIN_EXTENSIONS]
LOCALIZED_GENERATED = [f"{base}{ext}" for base in LOCALIZED_PATHS for ext in ADMIN_EXTENSIONS]
ECOMMERCE_GENERATED = [f"{base}{ext}" for base in ECOMMERCE_PATHS for ext in ADMIN_EXTENSIONS]

# Combine all paths and remove duplicates
ALL_PATHS = list(set(
    ADMIN_PATHS + 
    GENERATED_PATHS + 
    LOCALIZED_PATHS + 
    LOCALIZED_GENERATED + 
    ECOMMERCE_PATHS + 
    ECOMMERCE_GENERATED
))
