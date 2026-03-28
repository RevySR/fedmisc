Name:           dput
Version:        1.2.4
Release:        1
Summary:        Debian Package Upload Tool

License:        GPL-3.0-only
URL:            https://packages.debian.org/source/sid/dput
Source0:        https://deb.debian.org/debian/pool/main/d/dput/dput_%{version}.tar.xz
Source1:        pyproject.toml

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-debian
BuildRequires:  python3-gpg
BuildRequires:  python3-pyxdg
BuildRequires:  pyproject-rpm-macros

Requires:       python3
Requires:       python3-debian
Requires:       python3-gpg
Requires:       python3-pyxdg

Suggests:       openssh-clients
Suggests:       rsync


%description
dput allows you to put one or more Debian packages into the archive.
It also includes dcut for managing the upload queue, and runs
compliance checks before upload.


%prep
%autosetup -n dput-%{version}
cp %{SOURCE1} .
# Use python3-pyxdg instead of the 'xdg' PyPI package; replace in install_requires
sed -i '/install_requires/,/\]/{s/"xdg"/"pyxdg"/}' setup.py
sed -i 's/import xdg$/import xdg.BaseDirectory/' dput/configfile.py
sed -i 's/xdg\.xdg_config_home()/xdg.BaseDirectory.xdg_config_home/' dput/configfile.py


%build
%pyproject_wheel


%install
%pyproject_install
ln -s execute-dput %{buildroot}%{_bindir}/dput
ln -s execute-dcut %{buildroot}%{_bindir}/dcut
install -D -m 0644 dput.cf %{buildroot}%{_sysconfdir}/dput.cf
install -D -m 0644 -t %{buildroot}%{_mandir}/man1/ doc/man/dput.1 doc/man/dcut.1
install -D -m 0644 -t %{buildroot}%{_mandir}/man5/ doc/man/dput.cf.5
install -D -m 0644 bash-completion/dput.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/dput
install -D -m 0644 bash-completion/dcut.bash \
    %{buildroot}%{_datadir}/bash-completion/completions/dcut


%files
%doc README TODO doc/FAQ doc/THANKS
%license LICENSE.GPL-3
%config(noreplace) %{_sysconfdir}/dput.cf
%{_bindir}/dput
%{_bindir}/dcut
%{_bindir}/execute-dput
%{_bindir}/execute-dcut
%{python3_sitelib}/dput/
%{python3_sitelib}/dput-%{version}*/
%{_datadir}/bash-completion/completions/dput
%{_datadir}/bash-completion/completions/dcut
%{_mandir}/man1/dput.1*
%{_mandir}/man1/dcut.1*
%{_mandir}/man5/dput.cf.5*


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 1.2.4-1
- Initial packaging
