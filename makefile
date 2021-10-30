build:
	pyinstaller main.py --name toname --onefile


move:
	mv dist/toname /usr/local/bin/
