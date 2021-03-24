%define debug_package %{nil}
Name:		timeshift
Version:	20.11
Release:	1%{?dist}.9
Summary:	timeshitf

License:	GPLv2+
Source0:	%{name}-%{version}.tar.gz
#Patch101:     mytest.patch

BuildArch:	x86_64

BuildRequires:	libgee

%description
System restore tool for Linux. Creates filesystem snapshots using rsync+hardlinks, or BTRFS snapshots. Supports scheduled snapshots, multiple backup levels, and exclude filters. Snapshots can be restored while system is running or from Live CD/USB.

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
- Initial packaging
