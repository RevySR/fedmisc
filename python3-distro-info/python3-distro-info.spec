Name:           python3-distro-info
Version:        1.15
Release:        1
Summary:        Information about distributions' releases (Python 3 module)

License:        ISC
URL:            https://salsa.debian.org/debian/distro-info
Source0:        https://deb.debian.org/debian/pool/main/d/distro-info/distro-info_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3
Requires:       distro-info-data


%description
Python 3 module for parsing information about all releases of Debian,
Ubuntu and other distributions. Reads data from the distro-info-data
package.


%prep
%autosetup -n distro-info


%build
cd python
%py3_build


%install
cd python
%py3_install
install -D -m 0755 -t %{buildroot}%{_bindir} debian-distro-info ubuntu-distro-info


%files
%pycached %{python3_sitelib}/distro_info.py
%{python3_sitelib}/distro_info/
%{python3_sitelib}/distro_info-%{version}*/
%{_bindir}/debian-distro-info
%{_bindir}/ubuntu-distro-info


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 1.15-1
- Initial packaging
