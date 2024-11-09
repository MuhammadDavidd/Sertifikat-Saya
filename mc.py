from mcstatus import MinecraftServer
from colorama import Fore, Style, init
import time
import os

# Inisialisasi colorama
init(autoreset=True)

def print_header():
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)
    print(Fore.CYAN + Style.BRIGHT + "    🎮 Minecraft Server Status Checker   ")
    print(Fore.GREEN + Style.BRIGHT + "=" * 40)

def check_server_status():
    server_address = input(Fore.MAGENTA + "Masukkan alamat server Minecraft (contoh: play.example.com:25565): ")
    print(Fore.YELLOW + "\nMenghubungkan ke server...\n")
    time.sleep(1)
    try:
        server = MinecraftServer.lookup(server_address)
        status = server.status()

        print(Fore.GREEN + "\nServer Status:")
        print(Fore.YELLOW + "🟢 Server Online")
        print(Fore.CYAN + f"🌍 Alamat Server: {server_address}")
        print(Fore.CYAN + f"🔢 Versi: {status.version.name}")
        print(Fore.CYAN + f"👥 Pemain Online: {status.players.online}/{status.players.max}")
        print(Fore.CYAN + f"📜 Deskripsi: {status.description}")
        player_list = [player.name for player in status.players.sample] if status.players.sample else "Tidak ada pemain online"
        print(Fore.CYAN + f"👤 Daftar Pemain: {player_list}")
    except Exception as e:
        print(Fore.RED + "\nStatus Server:")
        print(Fore.RED + "🔴 Server Offline atau tidak dapat dijangkau.")
        print(Fore.RED + "Error:", e)

def show_info():
    print(Fore.CYAN + "\nInformasi Script:")
    print(Fore.YELLOW + "Script ini dibuat untuk memeriksa status server Minecraft.")
    print(Fore.YELLOW + "Fitur: Cek status online, jumlah pemain, versi server, dan deskripsi server.")
    print(Fore.YELLOW + "Dibuat oleh: [Nama Anda]\n")
    time.sleep(2)

def main_menu():
    while True:
        os.system("clear")
        print_header()
        print(Fore.GREEN + "\nMenu Utama:")
        print(Fore.CYAN + "[1] Cek Server")
        print(Fore.CYAN + "[2] Informasi Script")
        print(Fore.CYAN + "[3] Refresh")
        print(Fore.CYAN + "[4] Exit")

        choice = input(Fore.MAGENTA + "\nPilih opsi: ")

        if choice == "1":
            check_server_status()
        elif choice == "2":
            show_info()
        elif choice == "3":
            print(Fore.YELLOW + "\nRefreshing...\n")
            time.sleep(1)
        elif choice == "4":
            print(Fore.GREEN + "\nTerima kasih telah menggunakan script ini!")
            break
        else:
            print(Fore.RED + "\nPilihan tidak valid. Silakan coba lagi.")

        input(Fore.CYAN + "\nTekan Enter untuk kembali ke menu utama...")

# Jalankan menu utama
main_menu()
