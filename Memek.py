import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

username = 'Maestro'      

password = 'Tamvan'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("Username : ")

	if uname == username:

		pwd = raw_input("Password : ")



		if pwd == password:

			print "\033[1;32mBagus sudah masuk..", 

			sys.exit()



		else:

			print "\033[1;32mSalah anjing... [?]\033[00m"

			print "Silahkan segera log-in kembali...!!\n"

			restart()



	else:

		print "\033[1;32mSalah anjing... [?]\033[00m"

		print "Silahkan segera log-in kembali...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

