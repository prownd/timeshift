%define debug_package %{nil}
Name:		timeshift
Version:	20.11
Release:	1%{?dist}.9
Summary:	timeshitf

License:	GPLv2+
Source0:	%{name}-%{version}.tar.gz
#Source1:  name.source.1

#Patch101:     mytest.patch

BuildArch:	x86_64

Requires:	glib2
Requires:	dconf
Requires:   systemd

%description
timeshift backup and restore

%prep
%setup -q
#%patch101 -p1

%build
%make_build

%install
%make_install


%files
%{_sysconfdir}/*
%{_datadir}/*
%{_bindir}/*
#/usr/lib/*

#%post

#%postun


%changelog
* Wed Mar 24 2021 Han Jinpeng <hanjp@superred.com.cn> 20.11
- init timeshift
