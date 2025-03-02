# Base Admin Paths
ADMIN_PATHS = [
    # Standard Admin
    'admin/', 'administrator/', 'admincp/', 'admins/', 'adm/', 'administration/',
    'login/', 'login.php', 'login.asp', 'login.aspx', 'login.jsp', 'signin/',
    'sign-in/', 'sign_in/', 'ingreso/', 'connexion/', 'logon/', 'signin.php',
    'administrator.php', 'moderator/', 'webadmin/', 'authadmin/', 'auth/',
    'authuser/', 'autologin/', 'login_db/', 'database/', 'sistema/',

    # Blogging Platforms
    'wp-admin/', 'wp-login.php', 'wp-login/', 'wordpress/wp-admin/',
    'blog/wp-admin/', 'wp/wp-admin/', 'blog/admin/', 'blogger/admin/',
    'blogger.com/admin', 'tumblr/admin/', 'typepad/admin/', 'blog/login/',
    'ghost/signin/', 'medium/admin/', 'squarespace/admin/', 'weebly/admin/',
    'wix/admin/', 'blogspot.com/admin/', 'blogs/admin/', 'myblog/admin/',

    # CMS Systems
    'joomla/administrator/', 'cms/administrator/', 'drupal/admin/',
    'concrete/login/', 'modx/manager/', 'moodle/admin/', 'admin/cms/',
    'cms/admin/', 'umbraco/login/', 'sitemap/', 'content/', 'contents/',
    'contentadmin/', 'content-manager/', 'cms-admin/', 'cms_admin/',
    'kentico/admin/', 'sitecore/admin/', 'sharepoint/admin/', 'typo3/admin/',

    # E-commerce
    'magento/admin/', 'magento_admin/', 'admin_xxxxx/', 'store/admin/',
    'shop/admin/', 'shopping/admin/', 'shopify/admin/', 'prestashop/admin/',
    'opencart/admin/', 'woocommerce/admin/', 'cart/admin/', 'orders/admin/',
    'checkout/admin/', 'store-admin/', 'shop-admin/', 'seller/', 'sellers/',
    'vendor/', 'vendors/', 'supplier/', 'suppliers/', 'merchant/', 'merchants/',
    'store/administrator/', 'mall/admin/', 'market/admin/', 'marketplace/admin/',

    # Social Media/Forums
    'forum/admin/', 'community/admin/', 'social/admin/', 'phpbb/admin/',
    'vbulletin/admin/', 'moderator/login/', 'mod/control/', 'modcp/',
    'moderator_panel/', 'forum-admin/', 'forumadmin/', 'forums/admin/',
    'board/admin/', 'boardadmin/', 'community-admin/', 'social-admin/',
    'network/admin/', 'networking/admin/', 'community_admin/', 'groups/admin/',

    # Corporate/Business
    'intranet/', 'extranet/', 'corporate/admin/', 'business/admin/',
    'company/admin/', 'enterprise/admin/', 'corp/admin/', 'organization/admin/',
    'org/admin/', 'internal/', 'private/', 'secure/', 'protected/',
    'management/', 'manager/', 'manage/', 'project/', 'projects/',
    'projectmanager/', 'task/', 'tasks/', 'taskmanager/', 'portal/admin/',

    # Financial/Banking
    'bank/admin/', 'banking/admin/', 'finance/admin/', 'financial/admin/',
    'account/admin/', 'accounts/admin/', 'accounting/admin/', 'payment/admin/',
    'payments/admin/', 'transaction/admin/', 'transactions/admin/',
    'billing/admin/', 'invoice/admin/', 'invoices/admin/', 'payroll/admin/',

    # Educational
    'edu/admin/', 'education/admin/', 'school/admin/', 'university/admin/',
    'college/admin/', 'campus/admin/', 'student/admin/', 'teacher/admin/',
    'faculty/admin/', 'course/admin/', 'courses/admin/', 'lms/admin/',
    'learning/admin/', 'elearning/admin/', 'training/admin/', 'exam/admin/',

    # Healthcare
    'hospital/admin/', 'health/admin/', 'healthcare/admin/', 'medical/admin/',
    'clinic/admin/', 'doctor/admin/', 'patient/admin/', 'pharmacy/admin/',
    'medicine/admin/', 'dental/admin/', 'laboratory/admin/', 'lab/admin/',

    # Asian Platforms
    'baidu/admin/', 'qq/admin/', 'weibo/admin/', 'line/admin/',
    'kakao/admin/', 'naver/admin/', 'yahoo.co.jp/admin/',
    'rakuten/admin/', 'alibaba/admin/', 'taobao/admin/',
    'tencent/admin/', 'sina/admin/', 'sohu/admin/',

    # Modern Tech Platforms
    'ai/admin/', 'ml/admin/', 'iot/admin/', 'cloud/admin/',
    'data/admin/', 'analytics/admin/', 'dashboard/admin/',
    'metaverse/admin/', 'vr/admin/', 'ar/admin/',

    # SaaS and Modern CMS
    'strapi/admin/', 'contentful/admin/', 'prismic/admin/',
    'sanity/admin/', 'netlify/admin/', 'gatsby/admin/',
    'nextjs/admin/', 'nuxt/admin/', 'hugo/admin/',
    'saas/admin/', 'subscription/admin/', 'service/admin/',
    'platform/admin/', 'workspace/admin/', 'tenant/admin/'
]

# File Extensions
ADMIN_EXTENSIONS = [
    '.php', '.html', '.htm', '.asp', '.aspx', '.jsp', '.jspx', '.do',
    '.action', '.cfm', '.cgi', '.pl', '.py', '.rb', '.shtml', '.xml',
    '.json', '.wsdl', '.asmx', '.do', '.go', '.lua', '.sh', '.css',
    '.js', '.coffee', '.yaml', '.yml', '.conf', '.config', '.ini',
    '.log', '.db', '.sql', '.sqlite', '.sqlite3', '.properties',
    '.txt', '.md', '.asp.net', '.mvc', '.dll', '.exe', '.bin',
    '.cgi-bin', '.fcgi', '.wsgi', '.api', '.rest', '.graphql',
    '.rss', '.atom', '.pdf', '.doc', '.docx', '.xls', '.xlsx',
    '.ppt', '.pptx', '.odt', '.ods', '.odp', '.pages', '.numbers',
    '.key', '.backup', '.bak', '.old', '.new', '.tmp', '.temp',
    '.cache', '.inc', '.tpl', '.theme', '.module', '.class', '.jar',
    '.war', '.ear', '.rar', '.zip', '.tar', '.gz', '.7z', '.bz2',
    '.inc.php', '.master.php', '.local.php', '.production.php',
    '.development.php', '.stage.php', '.test.php', ''
]

# Regional Variations
REGIONAL_PREFIXES = [
    'admin-en', 'admin-fr', 'admin-es', 'admin-de', 'admin-it',
    'admin-ru', 'admin-cn', 'admin-jp', 'admin-kr', 'admin-ar',
    'admin-hi', 'admin-pt', 'admin-nl', 'admin-pl', 'admin-tr',
    'admin-th', 'admin-vi', 'admin-id', 'admin-my', 'admin-fa',
    'admin-sv', 'admin-da', 'admin-fi', 'admin-no', 'admin-is',
    'admin-cs', 'admin-sk', 'admin-hu', 'admin-ro', 'admin-bg',
    'admin-el', 'admin-lv', 'admin-lt', 'admin-et', 'admin-hr',
    'admin-sl', 'admin-sw', 'admin-zu', 'admin-xh', 'admin-af'
]

# Generate all possible combinations
def generate_all_paths():
    all_paths = set()
    
    # Add base admin paths
    all_paths.update(ADMIN_PATHS)
    
    # Add paths with extensions
    for base in ADMIN_PATHS:
        for ext in ADMIN_EXTENSIONS:
            all_paths.add(f"{base}{ext}")
    
    # Add regional variations
    for prefix in REGIONAL_PREFIXES:
        all_paths.add(f"{prefix}/")
        for ext in ADMIN_EXTENSIONS:
            all_paths.add(f"{prefix}/{ext}")
    
    return sorted(list(all_paths))

# Generate the final comprehensive list
ALL_ADMIN_PATHS = generate_all_paths()
