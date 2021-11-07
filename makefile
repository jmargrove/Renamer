build:
	pyinstaller main.py --name renamer --onefile

move:
	cp dist/renamer /usr/local/bin/

test: 
	pytest tests

seal:
	pip freeze > requirements.txt

release:
	gh release create v0.0.2-alpha ./dist/renamer --title "Grindelwald" --notes "This is an alpha release, toname is now the binary renamer. Only aphalnumeric chars are allowed for extensions" --prerelease 