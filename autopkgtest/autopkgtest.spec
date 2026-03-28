Name:           autopkgtest
Version:        5.55
Release:        1
Summary:        Automatic as-installed testing for Debian packages

License:        GPL-2.0-or-later
URL:            https://salsa.debian.org/ci-team/autopkgtest
Source0:        https://deb.debian.org/debian/pool/main/a/autopkgtest/autopkgtest_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3
BuildRequires:  python3-docutils

Requires:       apt
Requires:       dpkg-perl
Requires:       mawk >= 1.3.4
Requires:       procps-ng
Requires:       python3
Requires:       python3-debian
Requires:       python3-distro-info
Requires:       retry

Recommends:     fakeroot

Suggests:       docker-cli
Suggests:       lxc
Suggests:       mmdebstrap
Suggests:       ovmf
Suggests:       podman
Suggests:       qemu-system-x86
Suggests:       qemu-img
Suggests:       schroot
Suggests:       shadow-utils
Suggests:       util-linux


%description
autopkgtest runs tests on binary packages. The tests are run on the
package as installed on a testbed system (which may be found via a
virtualisation or containment system). The tests are expected to be
supplied in the corresponding Debian source package.

Depending on which virtualisation server you want to use, additional
packages may need to be installed (e.g. qemu-system-x86, lxc, podman).


%prep
%autosetup -n work


%build
make %{?_smp_mflags} \
    RST2HTML=rst2html


%install
%make_install prefix=%{_prefix}

# Substitute package version into the installed Python library
sed -i 's/@version@/%{version}/' \
    %{buildroot}%{_datadir}/%{name}/lib/adt_testbed.py


%files
%doc CREDITS
%doc doc/*.rst
%doc doc/*.html
%{_bindir}/autopkgtest
%{_bindir}/autopkgtest-build-*
%{_bindir}/autopkgtest-buildvm-ubuntu-cloud
%{_bindir}/autopkgtest-virt-*
%{_datadir}/%{name}/
%{_mandir}/man1/autopkgtest*.1*


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 5.55-1
- Initial packaging
