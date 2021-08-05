install:
	pip3 install .
publish:
	git push
	python3 -m build
	twine upload dist/*
	pip3 install --upgrade smidge
