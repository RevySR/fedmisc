Name:           sbuild
Version:        0.91.5
Release:        1
Summary:        Tool for building Debian binary packages from Debian sources

License:        GPL-2.0-or-later AND MIT
URL:            https://salsa.debian.org/debian/sbuild
Source0:        https://deb.debian.org/debian/pool/main/s/sbuild/sbuild_%{version}.tar.xz

BuildArch:      noarch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  dpkg-dev
BuildRequires:  perl-generators
BuildRequires:  perl-Data-Dumper
BuildRequires:  perl-Encode
BuildRequires:  perl-English
BuildRequires:  perl-Errno
BuildRequires:  perl-Exception-Class
BuildRequires:  perl-Fcntl
BuildRequires:  perl-File-Basename
BuildRequires:  perl-File-Copy
BuildRequires:  perl-File-Path
BuildRequires:  perl-File-Temp
BuildRequires:  perl-Filesys-Df
BuildRequires:  perl-Getopt-Long
BuildRequires:  perl-IO
BuildRequires:  perl-IO-Zlib
BuildRequires:  perl-MIME-Base64
BuildRequires:  perl-MIME-Lite
BuildRequires:  perl-Module-Load-Conditional
BuildRequires:  perl-PathTools
BuildRequires:  perl-Scalar-List-Utils
BuildRequires:  perl-Term-ANSIColor
BuildRequires:  perl-Time-HiRes
BuildRequires:  perl-YAML-Tiny
BuildRequires:  dpkg-perl
BuildRequires:  groff
BuildRequires:  perl-libwww-perl
BuildRequires:  perl-LWP-Protocol-https

Requires:       perl-Sbuild = %{version}-%{release}
Requires:       iproute
Requires:       shadow-utils
Requires:       util-linux
Requires:       apt
Requires:       perl-libwww-perl
Requires:       perl-LWP-Protocol-https

Recommends:     mmdebstrap >= 1.4.0
Recommends:     dpkg-dev

Suggests:       autopkgtest
Suggests:       sbuild-schroot


%description
sbuild uses chroots to build Debian packages in a controlled, clean
environment. It supports multiple backends including unshare (recommended),
schroot, and autopkgtest QEMU images.


%package -n perl-Sbuild
Summary:        Perl library for building Debian binary packages

Requires:       dpkg-perl >= 1.21.14
Requires:       perl-Exception-Class
Requires:       perl-Filesys-Df
Requires:       perl-MIME-Lite


%description -n perl-Sbuild
Core Perl library modules used by sbuild and buildd for building
Debian binary packages from source packages.


%package schroot
Summary:        Tool for building Debian binary packages (schroot backend)

Requires:       sbuild = %{version}-%{release}
Requires:       schroot

Recommends:     debootstrap


%description schroot
Additional tools for sbuild using the schroot backend, including
sbuild-createchroot, sbuild-adduser and other utilities for managing
schroot-based build environments.


%package qemu
Summary:        Utilities for using sbuild with QEMU images

Requires:       sbuild = %{version}-%{release}
Requires:       autopkgtest >= 5.17
Requires:       python3-pexpect
Requires:       python3-psutil
Requires:       qemu-system-x86
Requires:       qemu-system-aarch64
Requires:       qemu-system-riscv
Requires:       qemu-img


%description qemu
Utilities to facilitate the use of sbuild together with QEMU images
using sbuild's --chroot-mode=autopkgtest.


%package debian-developer-setup
Summary:        Convenience script to set up an sbuild environment (deprecated)

Requires:       sbuild-schroot = %{version}-%{release}
Requires:       cronie
Requires:       schroot
Requires:       debootstrap


%description debian-developer-setup
Deprecated convenience script to set up an sbuild environment using the
schroot backend. Please switch to the unshare backend instead.


%package -n buildd
Summary:        Daemon for automatically building Debian binary packages

Requires:       sbuild = %{version}-%{release}
Requires:       perl-Sbuild = %{version}-%{release}
Requires:       perl-YAML-Tiny
Requires:       shadow-utils
Requires:       cronie

Recommends:     sudo

Suggests:       schroot


%description -n buildd
buildd is a daemon which automatically builds Debian packages using the
wanna-build database to identify which packages need to be built.


%prep
%autosetup -n work
autoreconf -fi


%build
%configure
%make_build


%install
%make_install aptsolverdir=%{_libexecdir}/apt/solvers perlmoddir=%{perl_vendorlib}
install -d %{buildroot}%{_datadir}/%{name}
install -d %{buildroot}%{_localstatedir}/lib/buildd
echo '|/usr/bin/buildd-mail' > %{buildroot}%{_localstatedir}/lib/buildd/.forward
mv %{buildroot}%{_bindir}/sbuild-qemu-create-modscript \
   %{buildroot}%{_datadir}/%{name}/
ln -sf sbuild-abort %{buildroot}%{_bindir}/buildd-abort
install -D -m 0644 debian/buildd.cron.d \
    %{buildroot}%{_sysconfdir}/cron.d/buildd
install -D -m 0644 debian/buildd.default \
    %{buildroot}%{_sysconfdir}/default/buildd
install -D -m 0755 etc/sbuild-debian-developer-setup-update-all \
    %{buildroot}%{_sysconfdir}/cron.daily/sbuild-debian-developer-setup-update-all


%files
%doc README AUTHORS ChangeLog.in
%{_bindir}/sbuild
%{_libexecdir}/sbuild-usernsexec
%{_libexecdir}/apt/solvers/sbuild-cross-resolver
%{_sysconfdir}/sbuild/
%{_mandir}/man1/sbuild.1*
%{_mandir}/man5/sbuild.conf.5*


%files -n perl-Sbuild
%{perl_vendorlib}/Sbuild/
%{perl_vendorlib}/Sbuild.pm


%files schroot
%{_docdir}/%{name}/README.bins
%{_docdir}/%{name}/examples/
%{_bindir}/sbuild-abort
%{_bindir}/sbuild-apt
%{_bindir}/sbuild-checkpackages
%{_bindir}/sbuild-clean
%{_bindir}/sbuild-createchroot
%{_bindir}/sbuild-destroychroot
%{_bindir}/sbuild-distupgrade
%{_bindir}/sbuild-hold
%{_bindir}/sbuild-shell
%{_bindir}/sbuild-unhold
%{_bindir}/sbuild-update
%{_bindir}/sbuild-upgrade
%{_bindir}/sbuild-adduser
%{_datadir}/%{name}/dobuildlog
%{_mandir}/man1/sbuild-abort.1*
%{_mandir}/man1/sbuild-apt.1*
%{_mandir}/man1/sbuild-checkpackages.1*
%{_mandir}/man1/sbuild-clean.1*
%{_mandir}/man1/sbuild-distupgrade.1*
%{_mandir}/man1/sbuild-hold.1*
%{_mandir}/man1/sbuild-shell.1*
%{_mandir}/man1/sbuild-unhold.1*
%{_mandir}/man1/sbuild-update.1*
%{_mandir}/man1/sbuild-upgrade.1*
%{_mandir}/man7/sbuild-setup.7*
%{_mandir}/man8/sbuild-adduser.8*
%{_mandir}/man8/sbuild-createchroot.8*
%{_mandir}/man8/sbuild-destroychroot.8*


%files qemu
%{_bindir}/sbuild-qemu
%{_bindir}/sbuild-qemu-boot
%{_bindir}/sbuild-qemu-create
%{_bindir}/sbuild-qemu-update
%{_datadir}/%{name}/sbuild-qemu-create-modscript
%{_mandir}/man1/sbuild-qemu*.1*


%files debian-developer-setup
%{_bindir}/sbuild-debian-developer-setup
%{_sysconfdir}/cron.daily/sbuild-debian-developer-setup-update-all
%{_mandir}/man1/sbuild-debian-developer-setup.1*


%files -n buildd
%{_bindir}/buildd
%{_bindir}/buildd-abort
%{_bindir}/buildd-mail
%{_bindir}/buildd-update-chroots
%{_bindir}/buildd-uploader
%{_bindir}/buildd-vlog
%{_bindir}/buildd-watcher
%{perl_vendorlib}/Buildd/
%{perl_vendorlib}/Buildd.pm
%{_sysconfdir}/buildd/
%{_sysconfdir}/cron.d/buildd
%{_sysconfdir}/default/buildd
%dir %{_localstatedir}/lib/buildd/
%{_localstatedir}/lib/buildd/.forward
%{_datadir}/wanna-build/
%{_mandir}/man1/buildd*.1*
%{_mandir}/man5/buildd.conf.5*
%{_mandir}/man8/buildd-make-chroot.8*


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 0.91.5-1
- Initial packaging
