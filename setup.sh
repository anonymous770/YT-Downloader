apt-get upgrade
apt-get update
apt-get install python -y
pip install --upgrade pip
pip install pytube3
mv start-YT-Downloader.py .start-YT-Downloader.py
chmod +x .start-YT-Downloader.py
chmod +x yt
cp -r yt ~/../usr/bin
cp -r .start-YT-Downloader.py ~
echo "\n\t\033[1;33mType \033[1;31myt\033[0m \033[1;33mfor start tool.\033[0m\n"
