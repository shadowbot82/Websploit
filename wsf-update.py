# ! / usr / bin / env python
#
# WebSploit Modul Pembaruan FrameWork
# Dibuat oleh 0x0ptim0us (Fardin Allahverdinazhand)
# Email: 0x0ptim0us@Gmail.Com

mengimpor subproses
impor os
dari wcolors impor inti

def  update_websploit ():
	cetak wcolors.color. GREEN  +  " [*] Memperbarui kerangka kerja websploit, Harap Tunggu ... "  + wcolors.color. ENDC
	coba :
		subprocess.Popen ( " cd / tmp; git clone https://github.com/websploit/websploit.git;cp -R websploit / / usr / share; rm -rf / tmp / websploit / " , stdout = subprocess. PIPE , stderr = subprocess. PIPE , shell = True ) .wait ()
	kecuali  Exception , e:
		cetak wcolors.color. RED  +  " [!] Perbarui Gagal. " + Wcolors.color. ENDC
		lulus

	cetak wcolors.color. GREEN  +  " [*] Pembaruan berhasil diselesaikan. "  + Wcolors.color. ENDC
jika  __name__  ==  " __main__ " :
	update_websploit ()
