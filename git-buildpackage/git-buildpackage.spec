Name:           git-buildpackage
Version:        0.9.39
Release:        1
Summary:        Suite to help with Debian packages in Git repositories
License:        GPL-2.0-or-later AND MIT
URL:            https://honk.sigxcpu.org/piki/projects/git-buildpackage/
Source0:        https://deb.debian.org/debian/pool/main/g/git-buildpackage/git-buildpackage_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  pyproject-rpm-macros
BuildRequires:  make
BuildRequires:  docbook2X
BuildRequires:  docbook-dtds
BuildRequires:  libxslt
BuildRequires:  perl-Pod-Parser

Requires:       git >= 2.40.1
Requires:       python3-dateutil
Requires:       python3-pyyaml
Requires:       sensible-utils

Recommends:     pristine-tar
Recommends:     python3-requests

Suggests:       python3-notify2
Suggests:       sudo
Suggests:       unzip


%description
git-buildpackage (gbp) is a suite of tools that help with maintaining
Debian packages in Git repositories.

Included tools:
  gbp buildpackage, gbp import-orig, gbp export-orig, gbp import-dsc,
  gbp dch, gbp pq, gbp pull, gbp clone, gbp push, gbp tag,
  gbp pristine-tar, gbp create-remote-repo, gbp setup-gitattributes


%package rpm
Summary:        Suite to help with RPM packages in Git repositories
Requires:       %{name} = %{version}-%{release}
Requires:       cpio
Requires:       python3-rpm >= 4.16.1
Requires:       rpm >= 4.16.1

Suggests:       python3-notify2
Suggests:       unzip


%description rpm
git-buildpackage RPM tools for maintaining RPM packages in Git repositories.

Included tools:
  gbp buildpackage-rpm, gbp import-srpm, gbp pq-rpm


%prep
%autosetup -n git-buildpackage-%{version}
sed -i "/setup_requires/d" setup.py
# Replace entire docbook tool detection block (tab-indented lines before any
# target cause "recipe commences before first target" errors in make)
sed -i '/# Select docbook-to-man tool/,/^endif$/c DOCBOOK_TO_MAN = db2x_docbook2man' docs/Makefile


%build
WITHOUT_PYTESTS=1 %pyproject_wheel
# Build man pages; docbook2x-man (from docbook2X) outputs directly to current dir
cd docs
make gbp.1 gbp.conf.5 gbp-buildpackage-rpm.1 gbp-import-srpm.1 gbp-pq-rpm.1 gbp-rpm-ch.1 git-pbuilder.1
cd ..


%install
%pyproject_install

# setup.cfg installs gbp.conf to share/git_buildpackage/; move to /etc
install -D -m 0644 debian/gbp.conf \
    %{buildroot}%{_sysconfdir}/git-buildpackage/gbp.conf
rm -rf %{buildroot}%{_datadir}/git_buildpackage/

# gbp-builder-mock goes under datadir
mkdir -p %{buildroot}%{_datadir}/git-buildpackage/
mv %{buildroot}%{_bindir}/gbp-builder-mock \
    %{buildroot}%{_datadir}/git-buildpackage/gbp-builder-mock

# bash completion
install -D -m 0644 debian/gbp.completion \
    %{buildroot}%{_datadir}/bash-completion/completions/gbp

# zsh completion
install -D -m 0644 debian/zsh/_gbp \
    %{buildroot}%{_datadir}/zsh/site-functions/_gbp

# man pages
find docs -maxdepth 1 -name "*.1" -exec install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ {} \;
find docs -maxdepth 1 -name "*.5" -exec install -D -m 0644 -t %{buildroot}%{_mandir}/man5/ {} \;
ln -sf gbp.1 %{buildroot}%{_mandir}/man1/git-buildpackage.1


%files
%license COPYING
%doc README.md TODO
%config(noreplace) %{_sysconfdir}/git-buildpackage/gbp.conf
%{_bindir}/gbp
%{_bindir}/git-pbuilder
%{python3_sitelib}/gbp/
%{python3_sitelib}/gbp-%{version}*/
%exclude %{python3_sitelib}/gbp/rpm/
%exclude %{python3_sitelib}/gbp/scripts/buildpackage_rpm.py
%exclude %{python3_sitelib}/gbp/scripts/import_srpm.py
%exclude %{python3_sitelib}/gbp/scripts/pq_rpm.py
%exclude %{python3_sitelib}/gbp/scripts/rpm_ch.py
%{_datadir}/bash-completion/completions/gbp
%{_datadir}/zsh/site-functions/_gbp
%{_mandir}/man1/gbp*.1*
%{_mandir}/man1/git-buildpackage.1*
%{_mandir}/man1/git-pbuilder.1*
%{_mandir}/man5/gbp.conf.5*
%exclude %{_mandir}/man1/gbp-buildpackage-rpm.1*
%exclude %{_mandir}/man1/gbp-import-srpm.1*
%exclude %{_mandir}/man1/gbp-pq-rpm.1*
%exclude %{_mandir}/man1/gbp-rpm-ch.1*


%files rpm
%{_datadir}/git-buildpackage/gbp-builder-mock
%{python3_sitelib}/gbp/rpm/
%{python3_sitelib}/gbp/scripts/buildpackage_rpm.py
%{python3_sitelib}/gbp/scripts/import_srpm.py
%{python3_sitelib}/gbp/scripts/pq_rpm.py
%{python3_sitelib}/gbp/scripts/rpm_ch.py
%{_mandir}/man1/gbp-buildpackage-rpm.1*
%{_mandir}/man1/gbp-import-srpm.1*
%{_mandir}/man1/gbp-pq-rpm.1*
%{_mandir}/man1/gbp-rpm-ch.1*


%changelog
* Sun Mar 29 2026 Han Gao <rabenda.cn@gmail.com> - 0.9.39-1
- Initial packaging
