#!/usr/bin/env python3
from rich.console import Console
from rich.table import Table
from fake_useragent import UserAgent
from core.scanner import AdminScanner
from wordlists.paths import ALL_ADMIN_PATHS as ALL_PATHS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class AdminHunterPro:
    def __init__(self):
        self.console = Console()
        self.version = "1.0"
        self.user_agent = UserAgent()

    def banner(self):
        self.console.print("""
[bold cyan]
╔═══════════════════════════════════════════════════════════╗
║ auther=LIMBO-2018                   Admin Hunter Pro v1.0 ║
║        Professional Admin Panel Discovery Suite           ║
╠═══════════════════════════════════════════════════════════╣
║ [+] Advanced WAF Detection & Bypass                       ║
║ [+] Intelligent Response Analysis                         ║
║ [+] Dynamic Path Generation                              ║
║ [+] Multi-layered Verification                            ║
║ [+] Smart Crawling Technology                             ║
╚═══════════════════════════════════════════════════════════╝
[/bold cyan]""")

    def display_results(self, results):
        if not results:
            self.console.print("\n[red]No admin panels found.[/red]")
            return
           
        # display the table
        table = Table(show_header=True, header_style="bold magenta" )
        table.add_column("URL", style="cyan")
        table.add_column("Status", justify="center")
        table.add_column("Size", justify="right")
        table.add_column("Title")

        for result in results:
            table.add_row(
                result['url'],
                str(result['status']),
                str(result['length']),
                result['title']
            )

        self.console.print(table)
 
        self.console.print("\n[green]Found Admin Panels:[/green]")
        
        self.console.print("\n[yellow]Full URLs:[/yellow]")
        for result in results:
            self.console.print(f"[cyan]{result['url']}[/cyan]")
def main():
    hunter = AdminHunterPro()
    hunter.banner()
    
    target = input("\n[?] Enter target URL: ")
    if not target.startswith(('http://', 'https://')):
        target = 'https://' + target

    scanner = AdminScanner(target)
    scanner.start_scan(ALL_PATHS)
    hunter.display_results(scanner.results)

if __name__ == "__main__":
    main()
