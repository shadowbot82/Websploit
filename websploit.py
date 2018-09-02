# ! / usr / bin / env python
# 
#             ------------------------------------------------- -
#                             Kerangka WebSploit          
#             ------------------------------------------------- -
#         Hak Cipta (C) <2012> <0x0ptim0us (Fardin Allahverdinazhand)>
#
#         Program ini adalah perangkat lunak gratis: Anda dapat mendistribusikannya dan / atau memodifikasi
#         itu di bawah ketentuan Lisensi Publik Umum GNU yang diterbitkan oleh
#         the Free Software Foundation, baik versi 3 dari Lisensi, atau
#         versi yang lebih baru.
#
#         Program ini didistribusikan dengan harapan akan bermanfaat,
#        tetapi TANPA JAMINAN APAPUN; tanpa jaminan tersirat dari
#        MERCHANTABILITY atau FITNESS UNTUK TUJUAN TERTENTU. Lihat
#        Lisensi Publik Umum GNU untuk lebih jelasnya.
#
#         Anda seharusnya telah menerima salinan Lisensi Publik Umum GNU
#         bersama dengan program ini. Jika tidak, lihat <http://www.gnu.org/licenses/>.
#
#
#
#     WebSploit Advanced MITM Framework
#    
#    
#     Tentang Penulis:
#    
#     Pendiri: 0x0ptim0us (Fardin Allahverdinazhand)
#     Lokasi: Iran - Azarbaycan
#     Email: 0x0ptim0us@Gmail.com
#     Proyek Di SourceForge: https://sourceforge.net/p/websploit/wiki/Home/
#     Blog: www.websploit.ir
#
impor os
impor readline, rlcompleter
dari waktu tidur impor
dari wcolors impor inti
dari menu impor inti
dari header impor utama
dari core modules_database impor
dari bantuan impor  inti
dari peningkatan impor inti
dari pembaruan impor inti
dari inti impor sekitar
dari modul mengimpor apache_users
dari modul impor wmap
dari modules import directory_scanner
dari modul impor phpmyadmin
dari modul impor cloudflare_resolver
dari modul impor arp_dos
dari modul impor autopwn
dari modul impor mitm
dari modul impor mlitm
dari modul impor mfod
dari modul impor arp_poisoner
dari modul webkiller impor
dari modul impor brow_autopwn
dari modul import java_applet
dari modul impor wifi_jammer
dari modul impor wifi_dos
dari modul impor wifi_honeypot
dari modul impor mass_deauth
dari modul impor bluetooth_pod
dari modules.fakeupdate import fakeupdate

def  main ():
    coba :
        line_1 = wcolors.color. UNDERL  + wcolors.color. BIRU  +  " wsf "  + wcolors.color. ENDC
        line_1 + =  " > "
        terminal =  raw_input (baris_1)
        jika terminal [ 0 : 3 ] == ' gunakan ' :
            jika terminal [ 4 : 20 ] == ' web / apache_users ' :
                apache_users.apache_users ()
                utama()
            jika terminal [ 4 : 27 ] == ' web / cloudflare_resolver ' :
                cloudflare_resolver.cloudflare_resolver ()
                utama()
            terminal elif [ 4 : 20 ] == ' network / arp_dos ' :
                arp_dos.arp_dos ()
                utama()
            terminal elif [ 4 : 20 ] == ' exploit / autopwn ' :
                autopwn.autopwn ()
                utama()
            terminal elif [ 4 : 27 ] == ' exploit / browser_autopwn ' :
                brow_autopwn.brow_autopwn ()
                utama()
            elif terminal [ 4 : 19 ] ==  ' web / dir_scanner ' :
                directory_scanner.directory_scanner ()
                utama()
            terminal elif [ 4 : 12 ] == ' web / wmap ' :
                wmap.wmap ()
                utama()
            terminal elif [ 4 : 11 ] == ' web / pma ' :
                phpmyadmin.phpmyadmin ()
                utama()
            terminal elif [ 4 : 23 ] == ' exploit / java_applet ' :
                java_applet.java_applet ()
                utama()
            terminal elif [ 4 : 16 ] == ' network / mfod ' :
                mfod.mfod ()
                utama()
            terminal elif [ 4 : 16 ] == ' network / mitm ' :
                mitm.mitm ()
                utama()
            terminal elif [ 4 : 17 ] == ' network / mlitm ' :
                mlitm.mlitm ()
                utama()
            elif terminal [ 4 : 21 ] == ' network / webkiller ' :
                webkiller.webkiller ()
                utama()
            elif terminal [ 4 : 24 ] == ' network / arp_poisoner ' :
                arp_poisoner.arp_poisoner ()
                utama()
            elif terminal [ 4 : 22 ] == ' network / fakeupdate ' :
                fakeupdate.fakeupdate ()
                utama()
            terminal elif [ 4 : 20 ] == ' wifi / wifi_jammer ' :
                wifi_jammer.wifi_jammer ()
                utama()
            terminal elif [ 4 : 17 ] == ' wifi / wifi_dos ' :
                wifi_dos.wifi_dos ()
                utama()
            terminal elif [ 4 : 22 ] == ' wifi / wifi_honeypot ' :
                wifi_honeypot.wifi_honeypot ()
                utama()
            terminal elif [ 4 : 20 ] == ' wifi / mass_deauth ' :
                mass_deauth.mass_deauth ()
                utama()
            terminal elif [ 4 : 27 ] == ' bluetooth / bluetooth_pod ' :
                bluetooth_pod.bluetooth_pod ()
                utama()
        terminal elif [ 0 : 12 ] ==  ' tampilkan modul ' :
            modules_database.modules_database ()
            utama()
        terminal elif [ 0 : 4 ] == ' bantuan ' :
            help .help ()
            utama()
        terminal elif [ 0 : 2 ] == ' os ' :
            os.system (terminal [ 3 :])
            utama()
        terminal elif [ 0 : 7 ] == ' upgrade ' :
            upgrade.upgrade ()
            utama()
        elif terminal [ 0 : 6 ] == ' pembaruan ' :
            update.update ()
        terminal elif [ 0 : 5 ] == ' about ' :
            about.about ()
            utama()
        terminal elif [ 0 : 4 ] == ' keluar ' :
            keluar ()
        lain :
            cetak  " Perintah Salah => " , terminal
            utama()
    kecuali ( KeyboardInterrupt ):
        print (wcolors.color. RED  +  " \ n [*] (Ctrl + C) Terdeteksi, Mencoba Untuk Keluar ... "  + wcolors.color. ENDC )
        print (wcolors.color. YELLOW  +  " [*] Terima Kasih Telah Menggunakan Kerangka Websploit =) "  + wcolors.color. ENDC )
def  start ():
    header.main_header ()
    menu.main_info ()
    utama()
jika  __name__ == ' __main__ ' :
    mulai()
