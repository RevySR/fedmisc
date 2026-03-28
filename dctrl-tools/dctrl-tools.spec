Name:           dctrl-tools
Version:        2.24
Release:        1
Summary:        Command-line tools to process Debian package information
License:        GPL-2.0-or-later AND BSD-2-Clause
URL:            https://github.com/ajkaijanaho/dctrl-tools
Source0:        https://deb.debian.org/debian/pool/main/d/dctrl-tools/dctrl-tools_%{version}.orig.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  po4a


%description
Debian package information is generally stored in files having a
special file format, dubbed the Debian control file format (the dctrl
format). These tools operate on any files conforming to that format.

Included are:

  grep-dctrl     - Grep dctrl-format files
  grep-available - Grep the DPKG available database
  grep-status    - Grep the DPKG status database
  grep-aptavail  - Grep the APT available database
  grep-debtags   - Grep the Debtags package database
  sort-dctrl     - Sort dctrl-format files
  tbl-dctrl      - Tabulate dctrl-format files
  join-dctrl     - Join dctrl-format files
  sync-available - Sync the dpkg available database with the apt database


%prep
%autosetup -n dctrl-tools-%{version}


%build
%make_build prefix=%{_prefix} sysconfdir=%{_sysconfdir} sbindir=%{_sbindir}


%install
%make_install prefix=%{_prefix} sysconfdir=%{_sysconfdir} sbindir=%{_sbindir}


%find_lang dctrl-tools


%files -f dctrl-tools.lang
%license COPYING
%doc README TODO
%{_bindir}/grep-dctrl
%{_bindir}/grep-status
%{_bindir}/grep-available
%{_bindir}/grep-aptavail
%{_bindir}/grep-debtags
%{_bindir}/join-dctrl
%{_bindir}/sort-dctrl
%{_bindir}/tbl-dctrl
%{_bindir}/sync-available
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
%{_mandir}/*/man1/*.1*
%{_mandir}/*/man8/*.8*


%changelog
* Sat Mar 28 2026 Han Gao <rabenda.cn@gmail.com> - 2.24-1
- Initial packaging
