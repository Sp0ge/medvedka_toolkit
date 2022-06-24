sudo rm -rf medvedka_toolkit
echo remove medvedka_toolkit dir
sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade
sudo apt-get install python3 python3-pip
sudo git clone https://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@github.com/Sp0ge/medvedka_toolkit.git
sudo python3 -m pip install -r medvedka_toolkit/requirements.txt
echo pip intalled
sudo screen python3 app.py