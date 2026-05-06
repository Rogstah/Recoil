import os, sys, time, socket, platform, subprocess, struct
import urllib.request, urllib.parse, json, hashlib, base64
import threading, random, string, re, ipaddress, datetime

R = "\033[31m"
G = "\033[92m"
C = "\033[96m"
W = "\033[97m"
Y = "\033[93m"
M = "\033[95m"
DG = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def tw(text, color=W, delay=0.02, prefix=""):
    sys.stdout.write(f"{color}{prefix}")
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(RESET + "\n")
    sys.stdout.flush()

def info(msg): print(f"  {G}[+]{RESET} {W}{msg}{RESET}")
def warn(msg): print(f"  {Y}[!]{RESET} {W}{msg}{RESET}")
def err(msg):  print(f"  {R}[-]{RESET} {W}{msg}{RESET}")
def inp(msg):  return input(f"  {C}[?]{RESET} {W}{msg}{C} {RESET}").strip()
def sep():     print(f"  {DG}{'─'*54}{RESET}")

def boot():
    msgs = [
        ("Booting...", W),
        ("Don't Misuse Your Power", R),
        ("Humans Are Most Vulnerable", G),
        ("Improve, Don't Prove", R),
        ("Superpowers Need To Be Practiced", G),
        ("Security Is Just An Illusion", G),
        ("With Great Power Comes Great Responsibility", R),
        ("Be An Exception, Be An Example", G),
        ("Accept The Past, Move On", G),
        ("Good People Are Always Taken Advantage Of", G),
        ("Governments Control Our Media... Social Media Is Fake", G),
        ("Messing With Pride Is An Alltime Fool's Decision", R),
        ("Be An Example Before An Advisor", G),
        ("Time Doesn't Heal Anything, We Just Get Used To The Situation", R),
        ("A Monster Is Better Than An Arrogant God", G),
        ("Booting Completed :D", W),
    ]
    for msg, color in msgs:
        sys.stdout.write(f"{color}  [*] ")
        for ch in msg:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(0.025)
        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()
        time.sleep(0.4)
    time.sleep(0.8)
    clear()
    sys.stdout.write(f"{W}  [*] ")
    for ch in "Starting Tool...":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(RESET + "\n")
    time.sleep(1)
    clear()

def banner():
    print(f"{R}")
    print(r"  ██████╗ ███████╗ ██████╗ ██████╗ ██╗██╗     ")
    print(r"  ██╔══██╗██╔════╝██╔════╝██╔═══██╗██║██║     ")
    print(r"  ██████╔╝█████╗  ██║     ██║   ██║██║██║     ")
    print(r"  ██╔══██╗██╔══╝  ██║     ██║   ██║██║██║     ")
    print(r"  ██║  ██║███████╗╚██████╗╚██████╔╝██║███████╗")
    print(r"  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝╚══════╝")
    print(f"{RESET}")
    print(f"  {DG}{'─'*54}{RESET}")
    print(f"  {DG}v1.0  |  github.com/rogstah/recoil  |  use responsibly{RESET}")
    print(f"  {DG}{'─'*54}{RESET}")
    print()

def menu():
    cats = [
        ("NETWORK", [
            ("1",  "System Info"),
            ("2",  "Network Info"),
            ("3",  "Port Scanner"),
            ("4",  "Ping Host"),
            ("5",  "DNS Lookup"),
            ("6",  "Traceroute"),
            ("7",  "Whois Lookup"),
            ("8",  "IP Geolocation"),
            ("9",  "Reverse DNS"),
            ("10", "MAC Lookup"),
            ("11", "Subnet Calculator"),
            ("12", "HTTP Headers"),
            ("13", "Check Open Ports (Common)"),
            ("14", "SSL Certificate Info"),
            ("15", "Website Status Checker"),
        ]),
        ("OSINT", [
            ("16", "Email Validator"),
            ("17", "Username Availability"),
            ("18", "IP Reputation Check"),
            ("19", "Shodan-style Banner Grab"),
            ("20", "URL Expander"),
            ("21", "Find Subdomains"),
            ("22", "Google Dork Builder"),
            ("23", "Wayback Machine Lookup"),
            ("24", "Phone Number Info"),
            ("25", "Extract URLs from Page"),
        ]),
        ("CRYPTO & ENCODE", [
            ("26", "MD5 Hash"),
            ("27", "SHA1 Hash"),
            ("28", "SHA256 Hash"),
            ("29", "SHA512 Hash"),
            ("30", "Base64 Encode"),
            ("31", "Base64 Decode"),
            ("32", "URL Encode"),
            ("33", "URL Decode"),
            ("34", "Hex Encode"),
            ("35", "Hex Decode"),
            ("36", "ROT13"),
            ("37", "Caesar Cipher"),
            ("38", "Binary Encode"),
            ("39", "Binary Decode"),
            ("40", "XOR Encrypt/Decrypt"),
        ]),
        ("GENERATORS", [
            ("41", "Random Password"),
            ("42", "Random UUID"),
            ("43", "Random MAC Address"),
            ("44", "Random IP Address"),
            ("45", "Random Username"),
            ("46", "Random Email"),
            ("47", "Lorem Ipsum Generator"),
            ("48", "QR Code (URL)"),
            ("49", "Wordlist Generator"),
            ("50", "JWT Decoder"),
        ]),
        ("SYSTEM", [
            ("51", "System Info"),
            ("52", "Running Processes"),
            ("53", "Disk Usage"),
            ("54", "RAM Usage"),
            ("55", "CPU Info"),
            ("56", "Environment Variables"),
            ("57", "Current User Info"),
            ("58", "Open Network Connections"),
            ("59", "Startup Programs (Windows)"),
            ("60", "Installed Python Packages"),
        ]),
        ("FILE TOOLS", [
            ("61", "File Hash (MD5/SHA256)"),
            ("62", "File Info"),
            ("63", "Strings in File"),
            ("64", "Search Text in Files"),
            ("65", "Count Lines in File"),
            ("66", "Base64 Encode File"),
            ("67", "Base64 Decode File"),
            ("68", "Hex Dump"),
            ("69", "Split File"),
            ("70", "Merge Files"),
        ]),
        ("TEXT TOOLS", [
            ("71", "Word Count"),
            ("72", "Char Frequency"),
            ("73", "Reverse Text"),
            ("74", "Text to ASCII Art"),
            ("75", "Case Converter"),
            ("76", "Palindrome Check"),
            ("77", "Remove Duplicates"),
            ("78", "Sort Lines"),
            ("79", "Regex Tester"),
            ("80", "Extract Emails from Text"),
        ]),
        ("WEB TOOLS", [
            ("81", "Curl-like GET Request"),
            ("82", "POST Request"),
            ("83", "Download File"),
            ("84", "Check Redirect Chain"),
            ("85", "Extract Links from URL"),
            ("86", "Page Title Grabber"),
            ("87", "Response Time Checker"),
            ("88", "Robots.txt Viewer"),
            ("89", "Sitemap Viewer"),
            ("90", "Find Login Pages"),
        ]),
        ("MISC", [
            ("91",  "IP to Binary"),
            ("92",  "Binary to IP"),
            ("93",  "Epoch to Date"),
            ("94",  "Date to Epoch"),
            ("95",  "Calculate CIDR"),
            ("96",  "Number Base Converter"),
            ("97",  "ASCII Table"),
            ("98",  "Color Code Converter"),
            ("99",  "Morse Code Encoder"),
            ("100", "Morse Code Decoder"),
            ("0",   "Exit"),
        ]),
    ]
    for cat_name, items in cats:
        print(f"  {R}┌─ {W}{BOLD}{cat_name}{RESET}")
        for num, name in items:
            print(f"  {R}│  {DG}[{C}{num:>3}{DG}]  {W}{name}{RESET}")
        print(f"  {R}└{'─'*40}{RESET}")
        print()

def back():
    print()
    input(f"  {Y}[*] Press Enter to go back...{RESET}")

def require_target(label="Target"):
    return inp(f"{label}: ")

def n1_system_info():
    import platform, socket
    info("System Information"); sep()
    data = [
        ("OS",        platform.system() + " " + platform.release()),
        ("Version",   platform.version()[:60]),
        ("Machine",   platform.machine()),
        ("Processor", platform.processor()[:60] or "N/A"),
        ("Hostname",  socket.gethostname()),
        ("Python",    platform.python_version()),
        ("Node",      platform.node()),
    ]
    for k, v in data:
        print(f"  {DG}{k:<12}{RESET}: {C}{v}{RESET}")

def n2_network_info():
    import socket
    info("Network Information"); sep()
    h = socket.gethostname()
    try: lip = socket.gethostbyname(h)
    except: lip = "N/A"
    try: pip = urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
    except: pip = "N/A"
    print(f"  {DG}{'Hostname':<14}{RESET}: {C}{h}{RESET}")
    print(f"  {DG}{'Local IP':<14}{RESET}: {C}{lip}{RESET}")
    print(f"  {DG}{'Public IP':<14}{RESET}: {C}{pip}{RESET}")
    try:
        for iface in socket.getaddrinfo(socket.gethostname(), None):
            print(f"  {DG}{'Interface':<14}{RESET}: {C}{iface[4][0]}{RESET}")
    except: pass

def n3_port_scanner():
    info("Port Scanner"); sep()
    target = require_target("Host")
    start = inp("Start port")
    end = inp("End port")
    try:
        start, end = int(start), int(end)
        ip = socket.gethostbyname(target)
    except Exception as e:
        err(str(e)); return
    print(f"\n  {C}Scanning {ip} ports {start}–{end}...{RESET}\n")
    found = []
    for p in range(start, end+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.4)
        if s.connect_ex((ip, p)) == 0:
            try: svc = socket.getservbyport(p)
            except: svc = "unknown"
            print(f"  {G}[OPEN]{RESET}  {C}{p:<6}{RESET}  {DG}{svc}{RESET}")
            found.append(p)
        s.close()
    sep()
    info(f"{len(found)} open port(s) found.")

def n4_ping():
    info("Ping Host"); sep()
    target = require_target("Host")
    flag = "-n" if os.name == "nt" else "-c"
    os.system(f"ping {flag} 4 {target}")

def n5_dns():
    import socket
    info("DNS Lookup"); sep()
    target = require_target("Domain")
    try:
        results = socket.getaddrinfo(target, None)
        ips = list(set(r[4][0] for r in results))
        for ip in ips:
            print(f"  {G}[A]{RESET}  {C}{target}{RESET}  {DG}→{RESET}  {W}{ip}{RESET}")
    except Exception as e: err(str(e))

def n6_traceroute():
    info("Traceroute"); sep()
    target = require_target("Host")
    cmd = f"tracert {target}" if os.name == "nt" else f"traceroute {target}"
    os.system(cmd)

def n7_whois():
    info("Whois Lookup"); sep()
    target = require_target("Domain/IP")
    try:
        import whois
        w = whois.whois(target)
        print(f"  {C}{w}{RESET}")
    except ImportError:
        warn("pip install python-whois  required")
        try:
            r = urllib.request.urlopen(f"https://api.whoisjson.com/v1/?api=free&host={target}", timeout=8)
            data = json.loads(r.read().decode())
            for k, v in data.items():
                if v: print(f"  {DG}{k:<20}{RESET}: {W}{str(v)[:80]}{RESET}")
        except Exception as e: err(str(e))

def n8_geoip():
    info("IP Geolocation"); sep()
    target = require_target("IP")
    try:
        r = urllib.request.urlopen(f"http://ip-api.com/json/{target}?fields=status,country,regionName,city,zip,lat,lon,isp,org,as,query", timeout=8)
        d = json.loads(r.read().decode())
        for k, v in d.items():
            if v and k != "status": print(f"  {DG}{k:<12}{RESET}: {C}{v}{RESET}")
    except Exception as e: err(str(e))

def n9_rdns():
    info("Reverse DNS"); sep()
    target = require_target("IP")
    try:
        host = socket.gethostbyaddr(target)
        info(f"{target} → {host[0]}")
        for alias in host[1]: print(f"  {DG}alias{RESET}: {C}{alias}{RESET}")
    except Exception as e: err(str(e))

def n10_mac():
    info("MAC Lookup"); sep()
    mac = require_target("MAC (first 6 chars, e.g. AA:BB:CC)")
    mac_clean = mac.replace(":", "").replace("-", "")[:6]
    try:
        r = urllib.request.urlopen(f"https://api.macvendors.com/{urllib.parse.quote(mac_clean)}", timeout=6)
        vendor = r.read().decode()
        info(f"Vendor: {vendor}")
    except Exception as e: err(str(e))

def n11_subnet():
    info("Subnet Calculator"); sep()
    cidr = require_target("CIDR (e.g. 192.168.1.0/24)")
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        print(f"  {DG}Network    {RESET}: {C}{net.network_address}{RESET}")
        print(f"  {DG}Broadcast  {RESET}: {C}{net.broadcast_address}{RESET}")
        print(f"  {DG}Netmask    {RESET}: {C}{net.netmask}{RESET}")
        print(f"  {DG}Hosts      {RESET}: {C}{net.num_addresses - 2}{RESET}")
        print(f"  {DG}First host {RESET}: {C}{list(net.hosts())[0]}{RESET}")
        print(f"  {DG}Last host  {RESET}: {C}{list(net.hosts())[-1]}{RESET}")
    except Exception as e: err(str(e))

def n12_http_headers():
    info("HTTP Headers"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=8)
        for k, v in r.headers.items():
            print(f"  {DG}{k:<28}{RESET}: {C}{v}{RESET}")
    except Exception as e: err(str(e))

def n13_common_ports():
    info("Common Open Ports"); sep()
    target = require_target("Host")
    common = [21,22,23,25,53,80,110,143,443,445,3306,3389,5900,8080,8443]
    try: ip = socket.gethostbyname(target)
    except Exception as e: err(str(e)); return
    print(f"\n  {C}Scanning {ip}...{RESET}\n")
    for p in common:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((ip, p))
        status = f"{G}OPEN{RESET}" if result == 0 else f"{R}CLOSED{RESET}"
        try: svc = socket.getservbyport(p)
        except: svc = "?"
        print(f"  {C}{p:<6}{RESET}  {DG}{svc:<12}{RESET}  {status}")
        s.close()

def n14_ssl():
    import ssl
    info("SSL Certificate Info"); sep()
    host = require_target("Host")
    port = 443
    try:
        ctx = ssl.create_default_context()
        with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
            s.connect((host, port))
            cert = s.getpeercert()
        for k, v in cert.items():
            print(f"  {DG}{k:<24}{RESET}: {C}{v}{RESET}")
    except Exception as e: err(str(e))

def n15_website_status():
    info("Website Status"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        start = time.time()
        r = urllib.request.urlopen(url, timeout=8)
        elapsed = round((time.time() - start) * 1000)
        info(f"Status : {r.status}")
        info(f"Time   : {elapsed}ms")
    except urllib.error.HTTPError as e: warn(f"HTTP {e.code}")
    except Exception as e: err(str(e))

def o16_email_validator():
    info("Email Validator"); sep()
    email = require_target("Email")
    pattern = r"^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        info(f"Valid format: {email}")
        domain = email.split("@")[1]
        try:
            ip = socket.gethostbyname(domain)
            info(f"Domain resolves: {ip}")
        except: warn("Domain does not resolve")
    else:
        err("Invalid email format")

def o17_username():
    info("Username Availability"); sep()
    uname = require_target("Username")
    sites = {
        "GitHub":    f"https://github.com/{uname}",
        "Twitter":   f"https://twitter.com/{uname}",
        "Instagram": f"https://www.instagram.com/{uname}",
        "Reddit":    f"https://www.reddit.com/user/{uname}",
        "TikTok":    f"https://www.tiktok.com/@{uname}",
    }
    for site, url in sites.items():
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            r = urllib.request.urlopen(req, timeout=6)
            status = f"{R}TAKEN{RESET}" if r.status == 200 else f"{G}MAYBE FREE{RESET}"
        except urllib.error.HTTPError as e:
            status = f"{G}FREE{RESET}" if e.code == 404 else f"{Y}UNKNOWN ({e.code}){RESET}"
        except: status = f"{DG}TIMEOUT{RESET}"
        print(f"  {DG}{site:<12}{RESET}  {status}  {DG}{url}{RESET}")

def o18_ip_rep():
    info("IP Reputation"); sep()
    ip = require_target("IP")
    try:
        r = urllib.request.urlopen(f"http://ip-api.com/json/{ip}?fields=status,country,city,isp,proxy,hosting,mobile", timeout=8)
        d = json.loads(r.read().decode())
        for k, v in d.items():
            if k != "status":
                color = R if (k in ("proxy","hosting") and v) else C
                print(f"  {DG}{k:<10}{RESET}: {color}{v}{RESET}")
    except Exception as e: err(str(e))

def o19_banner_grab():
    info("Banner Grab"); sep()
    host = require_target("Host")
    port = inp("Port")
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, int(port)))
        try: s.send(b"HEAD / HTTP/1.0\r\n\r\n")
        except: pass
        banner_data = s.recv(1024).decode(errors="ignore")
        s.close()
        print(f"\n{DG}{'─'*56}{RESET}")
        print(f"  {G}{banner_data.strip()}{RESET}")
        print(f"{DG}{'─'*56}{RESET}")
    except Exception as e: err(str(e))

def o20_url_expander():
    info("URL Expander"); sep()
    url = require_target("Short URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=8)
        info(f"Final URL: {r.url}")
    except Exception as e: err(str(e))

def o21_subdomains():
    info("Subdomain Finder"); sep()
    domain = require_target("Domain")
    wordlist = ["www","mail","ftp","smtp","pop","ns1","ns2","vpn","api",
                "dev","staging","test","admin","portal","m","app","cloud",
                "cdn","blog","shop","store","support","help","docs","status"]
    print(f"\n  {C}Scanning subdomains for {domain}...{RESET}\n")
    found = []
    for sub in wordlist:
        host = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(host)
            print(f"  {G}[FOUND]{RESET}  {C}{host:<35}{RESET}  {DG}{ip}{RESET}")
            found.append(host)
        except: pass
    sep()
    info(f"{len(found)} subdomain(s) found.")

def o22_dork_builder():
    info("Google Dork Builder"); sep()
    print(f"  {DG}Templates:{RESET}")
    print(f"  {C}1{RESET}  site:example.com filetype:pdf")
    print(f"  {C}2{RESET}  intitle:\"index of\" site:example.com")
    print(f"  {C}3{RESET}  site:example.com inurl:admin")
    print(f"  {C}4{RESET}  intext:\"password\" filetype:txt site:example.com")
    print(f"  {C}5{RESET}  Custom")
    print()
    choice = inp("Template")
    site = inp("Target domain")
    dorks = {
        "1": f"site:{site} filetype:pdf",
        "2": f'intitle:"index of" site:{site}',
        "3": f"site:{site} inurl:admin",
        "4": f'intext:"password" filetype:txt site:{site}',
    }
    if choice == "5":
        dork = inp("Custom dork")
    else:
        dork = dorks.get(choice, f"site:{site}")
    url = "https://www.google.com/search?q=" + urllib.parse.quote(dork)
    info(f"Dork : {dork}")
    info(f"URL  : {url}")

def o23_wayback():
    info("Wayback Machine Lookup"); sep()
    url = require_target("URL")
    try:
        api = f"http://archive.org/wayback/available?url={urllib.parse.quote(url)}"
        r = urllib.request.urlopen(api, timeout=8)
        d = json.loads(r.read().decode())
        snap = d.get("archived_snapshots", {}).get("closest", {})
        if snap:
            info(f"Status : {snap.get('status')}")
            info(f"Date   : {snap.get('timestamp')}")
            info(f"URL    : {snap.get('url')}")
        else:
            warn("No snapshots found.")
    except Exception as e: err(str(e))

def o24_phone():
    info("Phone Number Info"); sep()
    phone = require_target("Phone (+countrycode number)")
    phone_clean = re.sub(r"\D", "", phone)
    country_codes = {"1":"USA/Canada","44":"UK","46":"Sweden","49":"Germany","33":"France","7":"Russia","86":"China","91":"India","61":"Australia","55":"Brazil"}
    for cc, country in sorted(country_codes.items(), key=lambda x: -len(x[0])):
        if phone_clean.startswith(cc):
            info(f"Country Code : +{cc}")
            info(f"Country      : {country}")
            info(f"Number       : {phone_clean[len(cc):]}")
            break
    else:
        info(f"Number: {phone_clean}")
    info(f"Length : {len(phone_clean)} digits")

def o25_extract_urls():
    info("Extract URLs from Page"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=8).read().decode(errors="ignore")
        urls = list(set(re.findall(r'https?://[^\s\'"<>]+', html)))
        for u in urls[:50]:
            print(f"  {G}→{RESET} {C}{u}{RESET}")
        info(f"Total: {len(urls)} URLs found")
    except Exception as e: err(str(e))

def c26_md5():
    info("MD5 Hash"); sep()
    text = require_target("Text")
    print(f"  {G}{hashlib.md5(text.encode()).hexdigest()}{RESET}")

def c27_sha1():
    info("SHA1 Hash"); sep()
    text = require_target("Text")
    print(f"  {G}{hashlib.sha1(text.encode()).hexdigest()}{RESET}")

def c28_sha256():
    info("SHA256 Hash"); sep()
    text = require_target("Text")
    print(f"  {G}{hashlib.sha256(text.encode()).hexdigest()}{RESET}")

def c29_sha512():
    info("SHA512 Hash"); sep()
    text = require_target("Text")
    print(f"  {G}{hashlib.sha512(text.encode()).hexdigest()}{RESET}")

def c30_b64enc():
    info("Base64 Encode"); sep()
    text = require_target("Text")
    print(f"  {G}{base64.b64encode(text.encode()).decode()}{RESET}")

def c31_b64dec():
    info("Base64 Decode"); sep()
    text = require_target("Base64")
    try: print(f"  {G}{base64.b64decode(text).decode()}{RESET}")
    except Exception as e: err(str(e))

def c32_url_enc():
    info("URL Encode"); sep()
    text = require_target("Text")
    print(f"  {G}{urllib.parse.quote(text)}{RESET}")

def c33_url_dec():
    info("URL Decode"); sep()
    text = require_target("Encoded")
    print(f"  {G}{urllib.parse.unquote(text)}{RESET}")

def c34_hex_enc():
    info("Hex Encode"); sep()
    text = require_target("Text")
    print(f"  {G}{text.encode().hex()}{RESET}")

def c35_hex_dec():
    info("Hex Decode"); sep()
    text = require_target("Hex")
    try: print(f"  {G}{bytes.fromhex(text).decode()}{RESET}")
    except Exception as e: err(str(e))

def c36_rot13():
    info("ROT13"); sep()
    text = require_target("Text")
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + 13) % 26 + base)
        else:
            result += ch
    print(f"  {G}{result}{RESET}")

def c37_caesar():
    info("Caesar Cipher"); sep()
    text = require_target("Text")
    shift = inp("Shift (number)")
    try:
        shift = int(shift)
        result = ""
        for ch in text:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                result += chr((ord(ch) - base + shift) % 26 + base)
            else:
                result += ch
        print(f"  {G}{result}{RESET}")
    except Exception as e: err(str(e))

def c38_bin_enc():
    info("Binary Encode"); sep()
    text = require_target("Text")
    result = " ".join(format(ord(c), "08b") for c in text)
    print(f"  {G}{result}{RESET}")

def c39_bin_dec():
    info("Binary Decode"); sep()
    text = require_target("Binary (space separated)")
    try:
        result = "".join(chr(int(b, 2)) for b in text.split())
        print(f"  {G}{result}{RESET}")
    except Exception as e: err(str(e))

def c40_xor():
    info("XOR Encrypt/Decrypt"); sep()
    text = require_target("Text")
    key = require_target("Key")
    result = "".join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(text))
    print(f"  {G}Result : {result}{RESET}")
    print(f"  {G}Hex    : {result.encode().hex()}{RESET}")

def g41_password():
    info("Random Password Generator"); sep()
    length = inp("Length (default 16)")
    try: length = int(length)
    except: length = 16
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+[]{}|;:,.<>?"
    password = "".join(random.choice(chars) for _ in range(length))
    print(f"\n  {G}{password}{RESET}\n")

def g42_uuid():
    import uuid
    info("Random UUID"); sep()
    for _ in range(5):
        print(f"  {G}{uuid.uuid4()}{RESET}")

def g43_mac_gen():
    info("Random MAC Address"); sep()
    for _ in range(5):
        mac = ":".join(format(random.randint(0, 255), "02x") for _ in range(6))
        print(f"  {G}{mac}{RESET}")

def g44_ip_gen():
    info("Random IP Address"); sep()
    for _ in range(5):
        ip = ".".join(str(random.randint(1, 254)) for _ in range(4))
        print(f"  {G}{ip}{RESET}")

def g45_username_gen():
    info("Random Username Generator"); sep()
    adj = ["dark","silent","ghost","rapid","elite","cyber","shadow","neon","void","zero"]
    nouns = ["wolf","hawk","byte","node","cipher","root","grid","flux","storm","hack"]
    for _ in range(8):
        name = random.choice(adj) + random.choice(nouns) + str(random.randint(10,999))
        print(f"  {G}{name}{RESET}")

def g46_email_gen():
    info("Random Email Generator"); sep()
    domains = ["gmail.com","yahoo.com","protonmail.com","outlook.com","tutanota.com"]
    for _ in range(6):
        name = "".join(random.choices(string.ascii_lowercase, k=random.randint(6,12)))
        email = f"{name}@{random.choice(domains)}"
        print(f"  {G}{email}{RESET}")

def g47_lorem():
    info("Lorem Ipsum Generator"); sep()
    n = inp("Paragraphs (default 2)")
    try: n = int(n)
    except: n = 2
    words = ["lorem","ipsum","dolor","sit","amet","consectetur","adipiscing","elit",
             "sed","do","eiusmod","tempor","incididunt","ut","labore","et","dolore",
             "magna","aliqua","enim","ad","minim","veniam","quis","nostrud"]
    for _ in range(n):
        para = " ".join(random.choices(words, k=random.randint(30,60)))
        print(f"\n  {W}{para.capitalize()}.{RESET}")

def g48_qr():
    info("QR Code URL"); sep()
    url = require_target("URL/Text")
    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={urllib.parse.quote(url)}"
    info(f"QR URL: {qr_url}")
    warn("Open the URL above in your browser to see the QR code.")

def g49_wordlist():
    info("Wordlist Generator"); sep()
    base = require_target("Base word")
    out = []
    for i in range(100):
        out.append(f"{base}{i}")
        out.append(f"{base}{i:02d}")
    for s in ["!", "@", "#", "123", "1234", "12345", "!", "!!"]:
        out.append(f"{base}{s}")
    print(f"\n  {C}Sample (first 20):{RESET}")
    for w in out[:20]: print(f"  {G}{w}{RESET}")
    save = inp("Save to file? (y/n)")
    if save.lower() == "y":
        fname = f"{base}_wordlist.txt"
        with open(fname, "w") as f:
            f.write("\n".join(out))
        info(f"Saved {len(out)} words to {fname}")

def g50_jwt():
    info("JWT Decoder"); sep()
    token = require_target("JWT Token")
    try:
        parts = token.split(".")
        if len(parts) != 3: raise ValueError("Invalid JWT")
        def decode_part(p):
            p += "=" * (4 - len(p) % 4)
            return json.loads(base64.urlsafe_b64decode(p).decode())
        header = decode_part(parts[0])
        payload = decode_part(parts[1])
        print(f"\n  {C}Header:{RESET}")
        for k, v in header.items(): print(f"  {DG}{k:<12}{RESET}: {W}{v}{RESET}")
        print(f"\n  {C}Payload:{RESET}")
        for k, v in payload.items():
            if k in ("exp","iat","nbf"):
                dt = datetime.datetime.utcfromtimestamp(v).strftime("%Y-%m-%d %H:%M:%S UTC")
                print(f"  {DG}{k:<12}{RESET}: {W}{v}{RESET}  {DG}({dt}){RESET}")
            else:
                print(f"  {DG}{k:<12}{RESET}: {W}{v}{RESET}")
        warn("Signature NOT verified.")
    except Exception as e: err(str(e))

def s51_sysinfo(): n1_system_info()

def s52_processes():
    info("Running Processes"); sep()
    cmd = "tasklist" if os.name == "nt" else "ps aux"
    os.system(cmd)

def s53_disk():
    info("Disk Usage"); sep()
    import shutil
    total, used, free = shutil.disk_usage("/")
    gb = 1024**3
    print(f"  {DG}Total{RESET}: {C}{total/gb:.1f} GB{RESET}")
    print(f"  {DG}Used {RESET}: {C}{used/gb:.1f} GB{RESET}")
    print(f"  {DG}Free {RESET}: {C}{free/gb:.1f} GB{RESET}")

def s54_ram():
    info("RAM Usage"); sep()
    try:
        import psutil
        vm = psutil.virtual_memory()
        print(f"  {DG}Total    {RESET}: {C}{vm.total/1024**3:.1f} GB{RESET}")
        print(f"  {DG}Used     {RESET}: {C}{vm.used/1024**3:.1f} GB{RESET}")
        print(f"  {DG}Available{RESET}: {C}{vm.available/1024**3:.1f} GB{RESET}")
        print(f"  {DG}Percent  {RESET}: {C}{vm.percent}%{RESET}")
    except ImportError:
        warn("pip install psutil  required for RAM info")

def s55_cpu():
    info("CPU Info"); sep()
    print(f"  {DG}Processor{RESET}: {C}{platform.processor() or 'N/A'}{RESET}")
    print(f"  {DG}Machine  {RESET}: {C}{platform.machine()}{RESET}")
    try:
        import psutil
        print(f"  {DG}Cores    {RESET}: {C}{psutil.cpu_count()}{RESET}")
        print(f"  {DG}Usage    {RESET}: {C}{psutil.cpu_percent(interval=1)}%{RESET}")
    except ImportError:
        warn("pip install psutil  for full CPU info")

def s56_env():
    info("Environment Variables"); sep()
    for k, v in sorted(os.environ.items()):
        print(f"  {DG}{k:<30}{RESET}: {C}{v[:60]}{RESET}")

def s57_whoami():
    info("Current User Info"); sep()
    import getpass
    print(f"  {DG}User    {RESET}: {C}{getpass.getuser()}{RESET}")
    print(f"  {DG}CWD     {RESET}: {C}{os.getcwd()}{RESET}")
    print(f"  {DG}OS      {RESET}: {C}{platform.system()} {platform.release()}{RESET}")
    print(f"  {DG}Python  {RESET}: {C}{sys.executable}{RESET}")

def s58_netconn():
    info("Open Network Connections"); sep()
    cmd = "netstat -ano" if os.name == "nt" else "netstat -tulnp"
    os.system(cmd)

def s59_startup():
    info("Startup Programs"); sep()
    if os.name == "nt":
        os.system('reg query HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run')
    else:
        warn("Linux: check /etc/init.d/ or systemctl list-unit-files")

def s60_pip():
    info("Installed Python Packages"); sep()
    os.system(f"{sys.executable} -m pip list")

def f61_file_hash():
    info("File Hash"); sep()
    path = require_target("File path")
    try:
        with open(path, "rb") as f:
            data = f.read()
        print(f"  {DG}MD5   {RESET}: {G}{hashlib.md5(data).hexdigest()}{RESET}")
        print(f"  {DG}SHA1  {RESET}: {G}{hashlib.sha1(data).hexdigest()}{RESET}")
        print(f"  {DG}SHA256{RESET}: {G}{hashlib.sha256(data).hexdigest()}{RESET}")
    except Exception as e: err(str(e))

def f62_file_info():
    info("File Info"); sep()
    path = require_target("File path")
    try:
        stat = os.stat(path)
        print(f"  {DG}Size    {RESET}: {C}{stat.st_size} bytes{RESET}")
        print(f"  {DG}Created {RESET}: {C}{datetime.datetime.fromtimestamp(stat.st_ctime)}{RESET}")
        print(f"  {DG}Modified{RESET}: {C}{datetime.datetime.fromtimestamp(stat.st_mtime)}{RESET}")
        print(f"  {DG}Mode    {RESET}: {C}{oct(stat.st_mode)}{RESET}")
    except Exception as e: err(str(e))

def f63_strings():
    info("Strings in File"); sep()
    path = require_target("File path")
    min_len = 4
    try:
        with open(path, "rb") as f:
            data = f.read()
        result = re.findall(b"[ -~]{" + str(min_len).encode() + b",}", data)
        for s in result[:100]:
            print(f"  {G}{s.decode()}{RESET}")
        info(f"Total strings: {len(result)}")
    except Exception as e: err(str(e))

def f64_search_text():
    info("Search Text in Files"); sep()
    directory = require_target("Directory")
    keyword = require_target("Keyword")
    try:
        for root, dirs, files in os.walk(directory):
            for fname in files:
                try:
                    fpath = os.path.join(root, fname)
                    with open(fpath, "r", errors="ignore") as f:
                        for i, line in enumerate(f, 1):
                            if keyword.lower() in line.lower():
                                print(f"  {G}{fpath}{RESET}:{C}{i}{RESET}: {line.strip()}")
                except: pass
    except Exception as e: err(str(e))

def f65_count_lines():
    info("Count Lines"); sep()
    path = require_target("File path")
    try:
        with open(path, "r", errors="ignore") as f:
            lines = f.readlines()
        info(f"Lines : {len(lines)}")
        info(f"Words : {sum(len(l.split()) for l in lines)}")
        info(f"Chars : {sum(len(l) for l in lines)}")
    except Exception as e: err(str(e))

def f66_b64_enc_file():
    info("Base64 Encode File"); sep()
    path = require_target("Input file")
    out = require_target("Output file")
    try:
        with open(path, "rb") as f: data = f.read()
        with open(out, "w") as f: f.write(base64.b64encode(data).decode())
        info(f"Saved to {out}")
    except Exception as e: err(str(e))

def f67_b64_dec_file():
    info("Base64 Decode File"); sep()
    path = require_target("Input file")
    out = require_target("Output file")
    try:
        with open(path, "r") as f: data = f.read()
        with open(out, "wb") as f: f.write(base64.b64decode(data))
        info(f"Saved to {out}")
    except Exception as e: err(str(e))

def f68_hexdump():
    info("Hex Dump"); sep()
    path = require_target("File path")
    try:
        with open(path, "rb") as f: data = f.read(512)
        for i in range(0, len(data), 16):
            chunk = data[i:i+16]
            hex_part = " ".join(f"{b:02x}" for b in chunk)
            asc_part = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
            print(f"  {DG}{i:08x}{RESET}  {C}{hex_part:<48}{RESET}  {G}{asc_part}{RESET}")
    except Exception as e: err(str(e))

def f69_split():
    info("Split File"); sep()
    path = require_target("File path")
    size = inp("Chunk size in bytes")
    try:
        size = int(size)
        with open(path, "rb") as f: data = f.read()
        for i, offset in enumerate(range(0, len(data), size)):
            chunk = data[offset:offset+size]
            fname = f"{path}.part{i}"
            with open(fname, "wb") as f: f.write(chunk)
            info(f"Wrote {fname} ({len(chunk)} bytes)")
    except Exception as e: err(str(e))

def f70_merge():
    info("Merge Files"); sep()
    files = require_target("Files (space separated)")
    out = require_target("Output file")
    try:
        with open(out, "wb") as outf:
            for fname in files.split():
                with open(fname.strip(), "rb") as f:
                    outf.write(f.read())
                info(f"Merged {fname}")
        info(f"Saved to {out}")
    except Exception as e: err(str(e))

def t71_wordcount():
    info("Word Count"); sep()
    text = require_target("Text or file path")
    if os.path.exists(text):
        with open(text, "r", errors="ignore") as f: text = f.read()
    info(f"Characters: {len(text)}")
    info(f"Words     : {len(text.split())}")
    info(f"Lines     : {len(text.splitlines())}")

def t72_charfreq():
    info("Character Frequency"); sep()
    text = require_target("Text")
    freq = {}
    for c in text:
        freq[c] = freq.get(c, 0) + 1
    for ch, count in sorted(freq.items(), key=lambda x: -x[1])[:20]:
        bar = "█" * count
        print(f"  {C}{repr(ch):<6}{RESET} {G}{bar}{RESET}  {DG}{count}{RESET}")

def t73_reverse():
    info("Reverse Text"); sep()
    text = require_target("Text")
    print(f"  {G}{text[::-1]}{RESET}")

def t74_ascii_art():
    info("Text to ASCII Art"); sep()
    try:
        import pyfiglet
        text = require_target("Text")
        print(f"{R}{pyfiglet.figlet_format(text)}{RESET}")
    except ImportError:
        warn("pip install pyfiglet  required")
        text = require_target("Text")
        print(f"  {G}{text.upper()}{RESET}")

def t75_case():
    info("Case Converter"); sep()
    text = require_target("Text")
    print(f"  {DG}Upper    {RESET}: {G}{text.upper()}{RESET}")
    print(f"  {DG}Lower    {RESET}: {G}{text.lower()}{RESET}")
    print(f"  {DG}Title    {RESET}: {G}{text.title()}{RESET}")
    print(f"  {DG}Swap     {RESET}: {G}{text.swapcase()}{RESET}")
    print(f"  {DG}Camel    {RESET}: {G}{''.join(w.capitalize() for w in text.split())}{RESET}")
    snake = "_".join(text.lower().split())
    print(f"  {DG}Snake    {RESET}: {G}{snake}{RESET}")

def t76_palindrome():
    info("Palindrome Check"); sep()
    text = require_target("Text")
    clean = re.sub(r"[^a-zA-Z0-9]", "", text).lower()
    if clean == clean[::-1]:
        info(f"✓ \"{text}\" IS a palindrome")
    else:
        warn(f"✗ \"{text}\" is NOT a palindrome")

def t77_dedup():
    info("Remove Duplicate Lines"); sep()
    path = require_target("File path")
    try:
        with open(path, "r", errors="ignore") as f:
            lines = f.readlines()
        unique = list(dict.fromkeys(lines))
        info(f"Before: {len(lines)}  After: {len(unique)}")
        save = inp("Save result? (y/n)")
        if save.lower() == "y":
            with open(path + ".dedup", "w") as f: f.writelines(unique)
            info(f"Saved to {path}.dedup")
    except Exception as e: err(str(e))

def t78_sort_lines():
    info("Sort Lines"); sep()
    path = require_target("File path")
    try:
        with open(path, "r", errors="ignore") as f: lines = f.readlines()
        lines.sort()
        for l in lines[:30]: print(f"  {G}{l.strip()}{RESET}")
        save = inp("Save sorted? (y/n)")
        if save.lower() == "y":
            with open(path + ".sorted", "w") as f: f.writelines(lines)
            info(f"Saved to {path}.sorted")
    except Exception as e: err(str(e))

def t79_regex():
    info("Regex Tester"); sep()
    text = require_target("Text")
    pattern = require_target("Regex pattern")
    try:
        matches = re.findall(pattern, text)
        if matches:
            info(f"{len(matches)} match(es) found:")
            for m in matches: print(f"  {G}{m}{RESET}")
        else:
            warn("No matches.")
    except Exception as e: err(str(e))

def t80_extract_emails():
    info("Extract Emails from Text"); sep()
    text = require_target("Text or file path")
    if os.path.exists(text):
        with open(text, "r", errors="ignore") as f: text = f.read()
    emails = list(set(re.findall(r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}", text)))
    for e in emails: print(f"  {G}{e}{RESET}")
    info(f"Total: {len(emails)}")

def w81_get():
    info("HTTP GET Request"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        r = urllib.request.urlopen(req, timeout=8)
        body = r.read().decode(errors="ignore")
        info(f"Status: {r.status}")
        print(f"\n{DG}{'─'*56}{RESET}")
        print(f"{C}{body[:2000]}{RESET}")
    except Exception as e: err(str(e))

def w82_post():
    info("HTTP POST Request"); sep()
    url = require_target("URL")
    data = require_target("POST data (key=val&key2=val2)")
    if not url.startswith("http"): url = "http://" + url
    try:
        encoded = urllib.parse.urlencode(dict(p.split("=",1) for p in data.split("&") if "=" in p)).encode()
        req = urllib.request.Request(url, data=encoded, headers={"User-Agent":"Mozilla/5.0","Content-Type":"application/x-www-form-urlencoded"})
        r = urllib.request.urlopen(req, timeout=8)
        body = r.read().decode(errors="ignore")
        info(f"Status: {r.status}")
        print(f"\n{C}{body[:1000]}{RESET}")
    except Exception as e: err(str(e))

def w83_download():
    info("Download File"); sep()
    url = require_target("URL")
    out = require_target("Output filename")
    try:
        def progress(count, block, total):
            pct = int(count * block * 100 / total) if total > 0 else 0
            sys.stdout.write(f"\r  {G}[{'█'*(pct//2):<50}]{RESET} {pct}%")
            sys.stdout.flush()
        urllib.request.urlretrieve(url, out, reporthook=progress)
        print()
        info(f"Saved to {out}")
    except Exception as e: err(str(e))

def w84_redirects():
    info("Redirect Chain"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    visited = []
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            visited.append((code, req.full_url))
            return super().redirect_request(req, fp, code, msg, headers, newurl)
    opener = urllib.request.build_opener(NoRedirect)
    try:
        r = opener.open(url, timeout=8)
        visited.append((r.status, r.url))
    except: pass
    for code, u in visited:
        print(f"  {C}{code}{RESET}  {G}→{RESET}  {W}{u}{RESET}")

def w85_extract_links():
    info("Extract Links from URL"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=8).read().decode(errors="ignore")
        links = list(set(re.findall(r'href=["\'](https?://[^"\']+)["\']', html)))
        for l in links[:50]: print(f"  {G}→{RESET} {C}{l}{RESET}")
        info(f"Total: {len(links)}")
    except Exception as e: err(str(e))

def w86_title():
    info("Page Title Grabber"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    try:
        req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
        html = urllib.request.urlopen(req, timeout=8).read().decode(errors="ignore")
        match = re.search(r"<title[^>]*>(.*?)</title>", html, re.IGNORECASE|re.DOTALL)
        if match: info(f"Title: {match.group(1).strip()}")
        else: warn("No title found.")
    except Exception as e: err(str(e))

def w87_response_time():
    info("Response Time Checker"); sep()
    url = require_target("URL")
    if not url.startswith("http"): url = "http://" + url
    for _ in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
            start = time.time()
            urllib.request.urlopen(req, timeout=10)
            ms = round((time.time()-start)*1000)
            color = G if ms < 500 else (Y if ms < 1500 else R)
            print(f"  {color}{ms}ms{RESET}")
        except Exception as e: err(str(e))
        time.sleep(0.5)

def w88_robots():
    info("Robots.txt Viewer"); sep()
    url = require_target("Domain (e.g. example.com)")
    if not url.startswith("http"): url = "http://" + url
    robots_url = url.rstrip("/") + "/robots.txt"
    try:
        req = urllib.request.Request(robots_url, headers={"User-Agent":"Mozilla/5.0"})
        content = urllib.request.urlopen(req, timeout=8).read().decode(errors="ignore")
        print(f"\n{G}{content}{RESET}")
    except Exception as e: err(str(e))

def w89_sitemap():
    info("Sitemap Viewer"); sep()
    url = require_target("Domain")
    if not url.startswith("http"): url = "http://" + url
    for path in ["/sitemap.xml", "/sitemap_index.xml"]:
        try:
            full = url.rstrip("/") + path
            req = urllib.request.Request(full, headers={"User-Agent":"Mozilla/5.0"})
            content = urllib.request.urlopen(req, timeout=8).read().decode(errors="ignore")
            urls = re.findall(r"<loc>(.*?)</loc>", content)
            info(f"Found {len(urls)} URLs in {path}")
            for u in urls[:30]: print(f"  {G}→{RESET} {C}{u}{RESET}")
            break
        except: pass
    else: warn("No sitemap found.")

def w90_login_pages():
    info("Find Login Pages"); sep()
    url = require_target("Domain")
    if not url.startswith("http"): url = "http://" + url
    paths = ["/login","/admin","/signin","/wp-login.php","/wp-admin",
             "/administrator","/user/login","/account/login","/auth/login",
             "/panel","/dashboard","/cp","/controlpanel","/manage"]
    print(f"\n  {C}Scanning...{RESET}\n")
    for path in paths:
        full = url.rstrip("/") + path
        try:
            req = urllib.request.Request(full, headers={"User-Agent":"Mozilla/5.0"})
            r = urllib.request.urlopen(req, timeout=5)
            print(f"  {G}[{r.status}]{RESET}  {C}{full}{RESET}")
        except urllib.error.HTTPError as e:
            if e.code not in (404,): print(f"  {Y}[{e.code}]{RESET}  {DG}{full}{RESET}")
        except: pass

def m91_ip2bin():
    info("IP to Binary"); sep()
    ip = require_target("IP")
    try:
        octets = ip.split(".")
        for o in octets:
            b = format(int(o), "08b")
            print(f"  {C}{o:<4}{RESET} → {G}{b}{RESET}")
        full = ".".join(format(int(o), "08b") for o in octets)
        print(f"\n  {W}{full}{RESET}")
    except Exception as e: err(str(e))

def m92_bin2ip():
    info("Binary to IP"); sep()
    binary = require_target("Binary IP (e.g. 11000000.10101000.00000001.00000001)")
    try:
        parts = binary.replace(" ","").split(".")
        ip = ".".join(str(int(p, 2)) for p in parts)
        info(f"IP: {ip}")
    except Exception as e: err(str(e))

def m93_epoch2date():
    info("Epoch to Date"); sep()
    epoch = require_target("Epoch timestamp")
    try:
        dt = datetime.datetime.utcfromtimestamp(int(epoch))
        info(f"UTC  : {dt.strftime('%Y-%m-%d %H:%M:%S')}")
        local = datetime.datetime.fromtimestamp(int(epoch))
        info(f"Local: {local.strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e: err(str(e))

def m94_date2epoch():
    info("Date to Epoch"); sep()
    dt_str = require_target("Date (YYYY-MM-DD HH:MM:SS)")
    try:
        dt = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
        import calendar
        epoch = int(calendar.timegm(dt.timetuple()))
        info(f"Epoch: {epoch}")
    except Exception as e: err(str(e))

def m95_cidr():
    info("CIDR Calculator"); sep()
    cidr = require_target("CIDR (e.g. 10.0.0.0/8)")
    try:
        net = ipaddress.ip_network(cidr, strict=False)
        info(f"Network   : {net.network_address}")
        info(f"Broadcast : {net.broadcast_address}")
        info(f"Netmask   : {net.netmask}")
        info(f"Wildcard  : {net.hostmask}")
        info(f"Hosts     : {net.num_addresses - 2:,}")
        info(f"CIDR      : /{net.prefixlen}")
    except Exception as e: err(str(e))

def m96_base_convert():
    info("Number Base Converter"); sep()
    num = require_target("Number")
    base = inp("From base (2/8/10/16)")
    try:
        n = int(num, int(base))
        print(f"  {DG}Binary {RESET}: {G}{bin(n)[2:]}{RESET}")
        print(f"  {DG}Octal  {RESET}: {G}{oct(n)[2:]}{RESET}")
        print(f"  {DG}Decimal{RESET}: {G}{n}{RESET}")
        print(f"  {DG}Hex    {RESET}: {G}{hex(n)[2:].upper()}{RESET}")
    except Exception as e: err(str(e))

def m97_ascii_table():
    info("ASCII Table"); sep()
    for i in range(32, 128):
        ch = chr(i)
        print(f"  {DG}{i:<5}{RESET}{C}{repr(ch):<6}{RESET}", end="")
        if (i - 31) % 8 == 0: print()
    print()

def m98_color_convert():
    info("Color Code Converter"); sep()
    val = require_target("HEX color (e.g. #FF5733) or RGB (255,87,51)")
    try:
        if val.startswith("#"):
            h = val.lstrip("#")
            r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
            info(f"HEX: #{h.upper()}")
            info(f"RGB: ({r}, {g}, {b})")
            info(f"HSL: (approx)")
        else:
            parts = [int(x.strip()) for x in val.split(",")]
            r, g, b = parts
            info(f"RGB: ({r}, {g}, {b})")
            info(f"HEX: #{r:02X}{g:02X}{b:02X}")
        preview = f"\033[48;2;{r};{g};{b}m          \033[0m"
        print(f"\n  Color preview: {preview}\n")
    except Exception as e: err(str(e))

def m99_morse_enc():
    info("Morse Code Encoder"); sep()
    text = require_target("Text")
    morse_map = {
        'A':'.-','B':'-...','C':'-.-.','D':'-..','E':'.','F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
        'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
        'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..',
        '0':'-----','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
        ' ': '/'
    }
    result = " ".join(morse_map.get(c.upper(), "?") for c in text)
    print(f"\n  {G}{result}{RESET}")

def m100_morse_dec():
    info("Morse Code Decoder"); sep()
    morse = require_target("Morse (dots/dashes, space between chars, / for word)")
    reverse = {
        '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
        '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
        '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
        '-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'
    }
    words = morse.split(" / ")
    result = " ".join("".join(reverse.get(c, "?") for c in word.split()) for word in words)
    print(f"\n  {G}{result}{RESET}")

ACTIONS = {
    "1": n1_system_info, "2": n2_network_info, "3": n3_port_scanner,
    "4": n4_ping, "5": n5_dns, "6": n6_traceroute, "7": n7_whois,
    "8": n8_geoip, "9": n9_rdns, "10": n10_mac, "11": n11_subnet,
    "12": n12_http_headers, "13": n13_common_ports, "14": n14_ssl,
    "15": n15_website_status, "16": o16_email_validator, "17": o17_username,
    "18": o18_ip_rep, "19": o19_banner_grab, "20": o20_url_expander,
    "21": o21_subdomains, "22": o22_dork_builder, "23": o23_wayback,
    "24": o24_phone, "25": o25_extract_urls, "26": c26_md5, "27": c27_sha1,
    "28": c28_sha256, "29": c29_sha512, "30": c30_b64enc, "31": c31_b64dec,
    "32": c32_url_enc, "33": c33_url_dec, "34": c34_hex_enc, "35": c35_hex_dec,
    "36": c36_rot13, "37": c37_caesar, "38": c38_bin_enc, "39": c39_bin_dec,
    "40": c40_xor, "41": g41_password, "42": g42_uuid, "43": g43_mac_gen,
    "44": g44_ip_gen, "45": g45_username_gen, "46": g46_email_gen,
    "47": g47_lorem, "48": g48_qr, "49": g49_wordlist, "50": g50_jwt,
    "51": s51_sysinfo, "52": s52_processes, "53": s53_disk, "54": s54_ram,
    "55": s55_cpu, "56": s56_env, "57": s57_whoami, "58": s58_netconn,
    "59": s59_startup, "60": s60_pip, "61": f61_file_hash, "62": f62_file_info,
    "63": f63_strings, "64": f64_search_text, "65": f65_count_lines,
    "66": f66_b64_enc_file, "67": f67_b64_dec_file, "68": f68_hexdump,
    "69": f69_split, "70": f70_merge, "71": t71_wordcount, "72": t72_charfreq,
    "73": t73_reverse, "74": t74_ascii_art, "75": t75_case, "76": t76_palindrome,
    "77": t77_dedup, "78": t78_sort_lines, "79": t79_regex, "80": t80_extract_emails,
    "81": w81_get, "82": w82_post, "83": w83_download, "84": w84_redirects,
    "85": w85_extract_links, "86": w86_title, "87": w87_response_time,
    "88": w88_robots, "89": w89_sitemap, "90": w90_login_pages,
    "91": m91_ip2bin, "92": m92_bin2ip, "93": m93_epoch2date, "94": m94_date2epoch,
    "95": m95_cidr, "96": m96_base_convert, "97": m97_ascii_table,
    "98": m98_color_convert, "99": m99_morse_enc, "100": m100_morse_dec,
}

def main():
    boot()
    while True:
        clear()
        banner()
        menu()
        choice = input(f"  {R}recoil{W}@{G}root {C}~#{RESET} ").strip().lstrip("0") or "0"
        if choice == "0":
            clear()
            tw("[*] Goodbye.", R, delay=0.04)
            time.sleep(0.5)
            sys.exit(0)
        if choice in ACTIONS:
            clear()
            banner()
            try:
                ACTIONS[choice]()
            except KeyboardInterrupt:
                warn("Interrupted.")
            back()
        else:
            warn("Invalid option.")
            time.sleep(0.6)

if __name__ == "__main__":
    main()