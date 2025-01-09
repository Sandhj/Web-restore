#Uodate Package
sudo apt update
#Instal Paket Virtual Envi
sudo apt install python3-venv
#Buat Lokasi Projek
mkdir -p /root/user/restore-web/
#Masuk Ke Lokasi Projek
cd /root/user/restore-web/
#buat python Env
python3 -m venv myenv
#Aktifkan Env 
source myenv/bin/activate
#Install Modul Yang Diinginkan
pip install flask

cd /root/user/restore-web/
wget -q https://raw.githubusercontent.com/Sandhj/Web-restore/main/

