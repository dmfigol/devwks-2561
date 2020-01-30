prepenv:
	python3 -m venv .venv; \
	. .venv/bin/activate; \
	pip install -U pip setuptools; \
	pip install -r requirements.txt; \
	xdg-open https://github.com/dmfigol/devwks-2561/blob/master/guide.md; \
	code .

prepenv-mac:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -U pip setuptools; \
	pip install -r requirements.txt; \
	xdg-open https://github.com/dmfigol/devwks-2561/blob/master/guide.md; \
	code .

provision:
	cd code; ../.venv/bin/python provision.py

vagrant:
	@echo "*** Stopping Existing VMs ***"
	vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate
	@echo "*** Bringing Up the Router ***"
	vagrant up

cleanup:
	@echo "*** Destroying the Vagrant box and python venv ***"
	vagrant destroy -f; \
	rm -rf .vagrant; \
	rm -rf .venv;

pull:
	git reset --hard; \
	git pull
