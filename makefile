.PHONY:

VERSION=$(shell head -1 VERSION)

 #  _   _                     ____        
 # | | | | _____   _____ _ __|  _ \ _   _ 
 # | |_| |/ _ \ \ / / _ \ '__| |_) | | | |
 # |  _  | (_) \ V /  __/ |  |  __/| |_| |
 # |_| |_|\___/ \_/ \___|_|  |_|    \__, |
 #                                  |___/ 

# Commands from most to least significant

all: 
	python setup.py build

# ┬─┐┌─┐┬  ┌─┐┌─┐┌─┐┌─┐  ┌─┐┌─┐┌┬┐┌─┐┬ ┬  ┌┬┐┌─┐┌─┐┌┬┐  ┬  ┬┌─┐┬─┐┌─┐┬┌─┐┌┐┌
# ├┬┘├┤ │  ├┤ ├─┤└─┐├┤   ├─┘├─┤ │ │  ├─┤   │ ├┤ └─┐ │   └┐┌┘├┤ ├┬┘└─┐││ ││││
# ┴└─└─┘┴─┘└─┘┴ ┴└─┘└─┘  ┴  ┴ ┴ ┴ └─┘┴ ┴   ┴ └─┘└─┘ ┴    └┘ └─┘┴└─└─┘┴└─┘┘└┘
release_test_patch: clean patch_tag commit push reg_and_upload_to_pypi clean

release_test: clean tag commit push reg_and_upload_to_pypi clean

reg_and_upload_to_pypi: register_test upload_test

patch_tag: semver_patch tag

tag: do_tag push_tags

test_install_from_pip:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	cd /tmp/ && pip install --install-option="--prefix=/tmp/" -i https://testpypi.python.org/pypi hoverpy
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python2.7/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test_local_tmp_install_python_2:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	mkdir -p /tmp/lib/python2.7/site-packages/
	cd /tmp/ && PYTHONPATH=/tmp/lib/python2.7/site-packages python setup.py install --prefix=/tmp
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python2.7/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test_local_tmp_install_python_3:
	rm -rf /tmp/hover*
	rm -rf /tmp/lib
	mkdir -p /tmp/lib/python3/site-packages/
	PYTHONPATH=/tmp/lib/python3/site-packages python3 setup.py install --prefix=/tmp
	cd /tmp/ && echo "import hoverpy;hoverpy.quick_test()" | PYTHONPATH=/tmp/lib/python3/site-packages python
	rm -rf /tmp/hover*
	rm -rf /tmp/lib

test:
	python setup.py test

docs: .PHONY
	python hoverpy/generateDocs.py

	pandoc --from=markdown --to=rst --output=docs/source/README.rst README.md

	pandoc --from=markdown --to=rst --output=docs/source/basic.rst examples/basic/README.md
	echo '.. basic\n\nbasic\n********\n\n' | cat - docs/source/basic.rst > temp && mv temp docs/source/basic.rst

	pandoc --from=markdown --to=rst --output=docs/source/readthedocs.rst examples/readthedocs/README.md
	echo '.. readthedocs\n\nreadthedocs\n********\n\n' | cat - docs/source/readthedocs.rst > temp && mv temp docs/source/readthedocs.rst

	pandoc --from=markdown --to=rst --output=docs/source/modify.rst examples/modify/README.md
	echo '.. modify\n\nmodify\n********\n\n' | cat - docs/source/modify.rst > temp && mv temp docs/source/modify.rst

	pandoc --from=markdown --to=rst --output=docs/source/delays.rst examples/delays/README.md
	echo '.. delays\n\ndelays\n********\n\n' | cat - docs/source/delays.rst > temp && mv temp docs/source/delays.rst

	pandoc --from=markdown --to=rst --output=docs/source/unittesting.rst examples/unittesting/README.md
	echo '.. unittesting\n\nunittesting\n********\n\n' | cat - docs/source/unittesting.rst > temp && mv temp docs/source/unittesting.rst

	pandoc --from=markdown --to=rst --output=docs/source/urllib2eg.rst examples/urllib2eg/README.md
	echo '.. urllib2\n\nurllib2\n********\n\n' | cat - docs/source/urllib2eg.rst > temp && mv temp docs/source/urllib2eg.rst

	pandoc --from=markdown --to=rst --output=docs/source/urllib3eg.rst examples/urllib3eg/README.md
	echo '.. urllib3\n\nurllib3\n********\n\n' | cat - docs/source/urllib3eg.rst > temp && mv temp docs/source/urllib3eg.rst

	cd docs; sphinx-apidoc --force -o source ../hoverpy/ ../hoverpy/tests;
	cd docs; make html;

### -------------------------------------------------------------------------------
## You'll need to save this into your ~/.pypirc if you'd like to push this to pypi

# [distutils]
# index-servers =
#   pypi
#   pypitest

# [pypi]
# repository=https://pypi.python.org/pypi
# username=
# password=

# [pypitest]
# repository=https://testpypi.python.org/pypi
# username=
# password=

### ------------------------------------
### ------------------------------------
## Probably nothing interesting below

register_test:
	python setup.py register -r pypitest

upload_test:
	python setup.py sdist upload -r pypitest

do_tag:
	git tag $(VERSION) -m "Adds a tag so that we can put this on PyPI."

push_tags:
	git push --tags origin 

commit:
	git add .
	git commit -am "updated"

push:
	git push

semver_patch:
	semver `head -1 VERSION` -i patch > VERSION
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ setup.py
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ hoverpy/config.py
	sed -i .bak s/$(VERSION)/`head -1 VERSION`/ docs/source/conf.py
	rm -f `find . -name '*.bak'`

clean:
	rm -rf build dist hoverpy.egg-info /tmp/hover* /tmp/lib .eggs hoverpy/__pycache__
	rm -f `find . -name "hoverfly.log"`
	rm -f `find . -name "*.pyc"`
	rm -rf `find . -name '__pycache__'`
	cd docs; make clean
