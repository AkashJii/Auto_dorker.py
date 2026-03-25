import urllib.parse

def generate_dorks(domain):
    # Yeh hamari dorks ki dictionary hai. Isme aur bhi add kar sakte ho.
    dorks = {
        "Exposed Directory Listing": 'intitle:"index of"',
        "Configuration Files": "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini",
        "Database Files": "ext:sql | ext:dbf | ext:mdb",
        "WordPress Config": "inurl:wp-config.php",
        "Log Files": "ext:log",
        "Backup & Old Files": "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup",
        "Login Pages": 'inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:admin',
        "Exposed Documents": "ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"
    }

    print("="*50)
    print(f"[*] Generating Auto-Dorks for: {domain}")
    print("="*50)

    # Har dork ko target domain ke sath mix karke Google URL banayenge
    for name, dork_query in dorks.items():
        # Query banegi: site:example.com intitle:"index of"
        full_query = f"site:{domain} {dork_query}"
        
        # URL mein space aur special characters ko encode karna zaroori hai
        encoded_query = urllib.parse.quote(full_query)
        google_url = f"https://www.google.com/search?q={encoded_query}"
        
        print(f"\n[+] {name}")
        print(f"    {google_url}")

if __name__ == "__main__":
    print("Welcome to Auto-Dorker - OSINT Recon Tool")
    target_domain = input("Enter target domain (e.g., example.com): ")
    
    if target_domain:
        generate_dorks(target_domain)
    else:
        print("Bhai, domain toh daalna padega!")
