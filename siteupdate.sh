rm -rf medvedka_toolkit
echo remove medvedka_toolkit dir
git clone https://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@github.com/Sp0ge/medvedka_toolkit.git
cd medvedka_toolkit
python3 -m pip install -r requirements.txt
echo pip intalled
screen python3 main.py