Name:           sarasa-gothic
Version:        1.0.36
Release:        1%{?dist}
Summary:        A CJK composite font based on Inter, Iosevka and Source Han Sans

License:        OFL-1.1
URL:            https://github.com/be5invis/Sarasa-Gothic
Source0:        https://github.com/be5invis/Sarasa-Gothic/releases/download/v%{version}/Sarasa-TTC-%{version}.zip

BuildArch:      noarch
Requires:       fontpackages-filesystem

%description
This is SARASA GOTHIC, a CJK composite font based on Inter, Iosevka and Source Han Sans.

%prep

%build
unzip %{SOURCE0}

%install
install -m 0755 -d %{buildroot}%{_fontbasedir}/%{name}

install -m 0644 -p Sarasa-*.ttc %{buildroot}%{_fontbasedir}/%{name}

%files
%{_fontbasedir}/%{name}/*.ttc

%changelog
* Sat Jan 24 2026 Eric Leung <contact@ericleung.dev> - 1.0.36-1
- Update to upstream version 1.0.36

* Sun Nov 23 2025 Eric Leung <contact@ericleung.dev> - 1.0.35-1
- Update to upstream version 1.0.35

* Sun Nov 09 2025 Eric Leung <contact@ericleung.dev> - 1.0.34-1
- Update to upstream version 1.0.34

* Sat Sep 13 2025 Eric Leung <contact@ericleung.dev> - 1.0.33-1
- Update to upstream version 1.0.33

* Sun Jul 20 2025 Eric Leung <contact@ericleung.dev> - 1.0.32-1
- Update to 1.0.32

* Tue Jun 11 2024 Eric Leung <contact@ericleung.dev> - 1.0.31-1
- Initial package
