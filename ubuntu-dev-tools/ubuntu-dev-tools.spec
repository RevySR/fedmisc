Name:           ubuntu-dev-tools
Version:        0.209
Release:        1
Summary:        Useful tools for Ubuntu developers
License:        GPL-2.0-or-later AND GPL-3.0-or-later
URL:            https://launchpad.net/ubuntu-dev-tools
Source0:        https://deb.debian.org/debian/pool/main/u/ubuntu-dev-tools/ubuntu-dev-tools_%{version}.tar.xz
Source1:        pyproject.toml

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-debian
BuildRequires:  python3-distro-info

Requires:       python3-ubuntutools = %{version}-%{release}
Requires:       dctrl-tools
Requires:       dpkg-dev
Requires:       binutils
Requires:       devscripts
Requires:       diffstat
Requires:       dput
Requires:       lsb-release
Requires:       python3
Requires:       python3-apt
Requires:       python3-debian
Requires:       python3-debianbts
Requires:       python3-distro-info
Requires:       python3-httplib2
Requires:       python3-launchpadlib
Requires:       python3-lazr-restfulclient
Requires:       python3-pyyaml
Requires:       sensible-utils
Requires:       tzdata

Recommends:     ca-certificates
Recommends:     debian-archive-keyring
Recommends:     debootstrap
Recommends:     genisoimage
Recommends:     patch
Recommends:     python3-dns
Recommends:     quilt
Recommends:     sbuild
Recommends:     sudo

Suggests:       qemu-user-static


%description
This is a collection of useful tools that Ubuntu developers use to make their
packaging work a lot easier. Such tools include backportpackage, check-mir,
grab-merge, mk-sbuild, pull-lp-source, requestsync, syncpackage, and more.


%package -n python3-ubuntutools
Summary:        Useful APIs for Ubuntu developer tools — Python 3 library
Requires:       python3-dateutil
Requires:       python3-debian
Requires:       python3-distro-info
Requires:       python3-httplib2
Requires:       python3-launchpadlib
Requires:       python3-lazr-restfulclient
Requires:       python3-requests
Requires:       sensible-utils


%description -n python3-ubuntutools
This package ships a collection of APIs, helpers and wrappers used to
develop useful utilities for Ubuntu developers. This package installs
the library for Python 3.


%prep
%autosetup -n ubuntu-dev-tools
cp %{SOURCE1} .
# setup.py reads version from debian/changelog; remove setup_requires if any
sed -i "/setup_requires/d" setup.py


%build
%pyproject_wheel


%install
%pyproject_install


%files
%license GPL-2 GPL-3
%doc README.updates TODO
%{_bindir}/backportpackage
%{_bindir}/check-mir
%{_bindir}/check-symbols
%{_bindir}/dch-repeat
%{_bindir}/grab-merge
%{_bindir}/grep-merges
%{_bindir}/import-bug-from-debian
%{_bindir}/lp-bitesize
%{_bindir}/merge-changelog
%{_bindir}/mk-sbuild
%{_bindir}/pbuilder-dist
%{_bindir}/pbuilder-dist-simple
%{_bindir}/pm-helper
%{_bindir}/pull-pkg
%{_bindir}/pull-debian-debdiff
%{_bindir}/pull-debian-source
%{_bindir}/pull-debian-debs
%{_bindir}/pull-debian-ddebs
%{_bindir}/pull-debian-udebs
%{_bindir}/pull-lp-source
%{_bindir}/pull-lp-debs
%{_bindir}/pull-lp-ddebs
%{_bindir}/pull-lp-udebs
%{_bindir}/pull-ppa-source
%{_bindir}/pull-ppa-debs
%{_bindir}/pull-ppa-ddebs
%{_bindir}/pull-ppa-udebs
%{_bindir}/pull-uca-source
%{_bindir}/pull-uca-debs
%{_bindir}/pull-uca-ddebs
%{_bindir}/pull-uca-udebs
%{_bindir}/requestbackport
%{_bindir}/requestsync
%{_bindir}/reverse-depends
%{_bindir}/running-autopkgtests
%{_bindir}/seeded-in-ubuntu
%{_bindir}/setup-packaging-environment
%{_bindir}/sponsor-patch
%{_bindir}/submittodebian
%{_bindir}/syncpackage
%{_bindir}/ubuntu-build
%{_bindir}/ubuntu-iso
%{_bindir}/ubuntu-upload-permission
%{_bindir}/update-maintainer
%{_datadir}/bash-completion/completions/pbuilder-dist
%{_datadir}/ubuntu-dev-tools/enforced-editing-wrapper
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*


%files -n python3-ubuntutools
%{python3_sitelib}/ubuntutools/
%{python3_sitelib}/ubuntu_dev_tools-%{version}*/


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 0.209-1
- Initial packaging
