def extract_title(html):
    try:
        start = html.find('<title>') + 7
        end = html.find('</title>')
        return html[start:end].strip()
    except:
        return "No Title"

def verify_admin_panel(response):
    admin_indicators = [
        'admin', 'login', 'dashboard', 'control panel',
        'username', 'password', 'administrator'
    ]
    
    content_length = len(response.content)
    if content_length < 50:
        return False
        
    text_lower = response.text.lower()
    indicator_count = sum(1 for indicator in admin_indicators if indicator in text_lower)
    
    return indicator_count >= 2
