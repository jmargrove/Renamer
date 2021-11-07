build:
	pyinstaller main.py --name renamer --onefile

move:
	mv dist/renamer /usr/local/bin/

test: 
	pytest tests

seal:
	pip freeze > requirements.txt
