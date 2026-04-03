srpm:
	dnf -y install spectool rpm-build
	spectool -g -R $(spec)
	rpmbuild -bs $(spec) --define "_sourcedir $$(dirname $(spec))" --define "_srcrpmdir $(outdir)"
