prepenv:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -U pip setuptools; \
	pip install -r requirements.txt

provision:
	cd code; ../.venv/bin/python provision.py

vagrant:
	@echo "*** Stopping Existing VMs ***"
	vboxmanage list runningvms | sed -E 's/.*\{(.*)\}/\1/' | xargs -L1 -I {} VBoxManage controlvm {} savestate
	@echo "*** Bringing Up the Router ***"
	vagrant up

cleanup:
	@echo "*** Destroying the Vagrant box ***"
	vagrant destroy -f