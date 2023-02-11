import sys, os, requests
from colorama import *

class functions:
    def download(link, name): #taken from my older project with some extra features added
        functions.clearconsole()
        print(
        '''
        ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
        ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
        ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░
        ██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗
        ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝
        ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
        ''')
        with open(name, "wb") as f:
            response = requests.get(link, stream=True)
            total_length = response.headers.get('content-length')
            length = int(total_length) / 1000000000
            length = round(length, 2)
            print(Fore.RESET+
            f'''
            ------------------------------------------------------------------------
            {Fore.YELLOW}File size: {Fore.RESET}{length} GB
            {Fore.YELLOW}File name: {Fore.RESET}{name}
            {Fore.YELLOW}File source: {Fore.RESET}https://archive.org (Exact links are in note.md file)
            {Fore.YELLOW}Working directory: {Fore.RESET}{os.getcwd()}
            {Fore.RED}DISCLAIMER: {Fore.RESET}I am not responsible for download speeds, all files are on Archive.org
            ------------------------------------------------------------------------
            '''
            )
            if total_length is None: # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=4096):
                    dl += len(data)
                    f.write(data)
                    done = int(50 * dl / total_length)
                    sys.stdout.write("\r            Progress bar: [%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()

    def clearconsole():
        os.system('cls' if os.name == 'nt' else 'clear')

functions.clearconsole()
init()

# Homepage
print(

    '''
        
    ░██████╗░███████╗████████╗  ██╗░░░██╗░█████╗░██╗░░░██╗██████╗░  ██╗░██████╗░█████╗░
    ██╔════╝░██╔════╝╚══██╔══╝  ╚██╗░██╔╝██╔══██╗██║░░░██║██╔══██╗  ██║██╔════╝██╔══██╗
    ██║░░██╗░█████╗░░░░░██║░░░  ░╚████╔╝░██║░░██║██║░░░██║██████╔╝  ██║╚█████╗░██║░░██║
    ██║░░╚██╗██╔══╝░░░░░██║░░░  ░░╚██╔╝░░██║░░██║██║░░░██║██╔══██╗  ██║░╚═══██╗██║░░██║
    ╚██████╔╝███████╗░░░██║░░░  ░░░██║░░░╚█████╔╝╚██████╔╝██║░░██║  ██║██████╔╝╚█████╔╝
    ░╚═════╝░╚══════╝░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝  ╚═╝╚═════╝░░╚════╝░

    '''
)
print(Fore.YELLOW + "   ISOs are multiversions (ALL) or Pro/Home and are in International (British) English")

print(Fore.LIGHTBLUE_EX + "\n\n    ---- WINDOWS SYSTEMS ----" + Fore.WHITE +
    '''

    [1] Windows 11 22H2 x64             [8] Windows 8.1 x64
    [2] Windows 11 21H2 x64             [9] Windows 8.1 x86
    [3] Leaked Windows 11         
                                        [10] Windows 7 x64
    [4] Windows 10 22H2 x64             [11] Windows 7 x86
    [5] Windows 10 20H2 x64
    [6] Windows 10 1507 x86             [12] Windows XP x86 SP3
    [7] Windows 10 1507 x64             [13] Windows XP x64 Edition

    '''
+ Fore.BLUE)

choice = int(input("\n> "))

match choice:
    case 1: functions.download(f"https://archive.org/download/windows-10-2022-update-version-22h2/Windows%2010%20%202022%20Update%20Version%2022H2.iso", "Windows11_22H2.iso")
    case 2: functions.download(f"https://archive.org/download/win-11-english-x-64_202111_202112/Win11_English_x64v1.iso", "Windows11_21H2.iso")
    case 3: functions.download(f"https://bit.ly/40Lnv3t", "Windows11_Leaked.iso")
    case 4: functions.download(f"https://archive.org/download/windows-10-2022-update-version-22h2/Windows%2010%20%202022%20Update%20Version%2022H2.iso", "Windows10_22H2.iso")
    case 5: functions.download(f"https://archive.org/download/win-10-20-h2-v2-english-x-64_20210429/Win10_20H2_v2_English_x64.iso", "Windows10_20H2.iso")
    case 6: functions.download(f"https://archive.org/download/windows-10-1507-home-and-pro/Win10_EnglishInternational_x32.iso", "Windows10_1507_x86.iso")
    case 7: functions.download(f"https://archive.org/download/windows-10-1507-home-and-pro/Win10_EnglishInternational_x64.iso", "Windows10_1507_x64.iso")
    case 8: functions.download(f"https://archive.org/download/win-8.1/Win8.1_EnglishInternational_x64.iso", "Windows8.1__x64.iso")
    case 9: functions.download(f"https://archive.org/download/win-8.1/Win8.1_EnglishInternational_x32.iso", "Windows8.1__x86.iso")
    case 10: functions.download(f"https://archive.org/download/Windows7-iso/win7_64_bit.iso", "Windows7__x64.iso")
    case 11: functions.download(f"https://archive.org/download/Windows7-iso/Win7Pro32bit.iso", "Windows7__x86.iso")
    case 12: functions.download(f"https://archive.org/download/WinXPProSP3x86/en_windows_xp_professional_with_service_pack_3_x86_cd_vl_x14-73974.iso", "WindowsXP_SP3_x86.iso")
    case 13: functions.download(f"https://archive.org/download/windows-xp-professional-x64-edition/Windows%20XP%20Professional%2064-bit%20Corporate%20Edition.iso", "WindowsXP_x64.iso")
