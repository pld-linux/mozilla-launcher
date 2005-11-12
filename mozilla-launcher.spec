Summary:	Script that launches mozilla or firefox
Name:		mozilla-launcher
Version:	1.45
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.gentoo.org/~agriffis/dist/%{name}-%{version}.bz2
# Source0-md5:	75f4e096742800278b0966d46508b570
URL:		http://dev.gentoo.org/~agriffis/dist/
Requires:	xtoolwait
# XFree86/X11 for xdpyinfo
Requires:	XFree86
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Script that launches mozilla or firefox.

%prep
%setup -qcT
bzip2 -dc %{SOURCE0} > %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install %{name} $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*
