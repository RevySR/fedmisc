Name:           distro-info-data
Version:        0.68
Release:        1
Summary:        Information about distributions' releases (data files)

License:        ISC
URL:            https://salsa.debian.org/debian/distro-info-data
Source0:        https://deb.debian.org/debian/pool/main/d/distro-info-data/distro-info-data_%{version}.tar.xz

BuildArch:      noarch


%description
CSV data files with information about all releases of Debian, Ubuntu,
Devuan and ELXR. Used by the distro-info tools and libraries.


%prep
%autosetup -n %{name}-%{version}


%build
# nothing to build


%install
install -d %{buildroot}%{_datadir}/distro-info
install -m 0644 debian.csv ubuntu.csv devuan.csv elxr.csv \
    %{buildroot}%{_datadir}/distro-info/


%files
%{_datadir}/distro-info/


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 0.68-1
- Initial packaging
