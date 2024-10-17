Name:		shelldap
Version:	1.5.1
Release:	1
Summary:	LDAP shell
License:	BSD
Group:		Networking/Other
URL:		https://projects.martini.nu/shelldap
Source:     shelldap
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A handy shell-like interface for browsing LDAP servers and editing their
content. It keeps command history, has sane autocompletes, credential caching,
site-wide and individual configs, and it's fun to say. Shelldap! Shelldap!
Shelldap!

%prep
%setup -c -T
perl -p \
    -e 's|^#!/usr/bin/env perl|#!%{_bindir}/perl|' \
    < %{SOURCE0} > shelldap

%build
pod2man shelldap shelldap.1

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 shelldap %{buildroot}%{_bindir}
install -m 644 shelldap.1 %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/shelldap
%{_mandir}/man1/shelldap.1*



%changelog
* Fri Sep 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.5-1mdv2012.0
+ Revision: 699964
- Update to 0.5

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.4-1
+ Revision: 645424
- update to new version 0.4

* Thu Jan 06 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-1mdv2011.0
+ Revision: 629052
- import shelldap

