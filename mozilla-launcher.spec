# TODO
# - pending bug https://bugs.gentoo.org/show_bug.cgi?id=112509
Summary:	Script that launches Mozilla or Firefox
Summary(pl.UTF-8):	Skrypt uruchiamiający Mozillę lub Firefoksa
Name:		mozilla-launcher
Version:	1.54
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.gentoo.org/~agriffis/dist/%{name}-%{version}.bz2
# Source0-md5:	414ed649bae2fe97359b17031999e9ac
Patch0:		%{name}-swiftfox.patch
URL:		http://dev.gentoo.org/~agriffis/dist/
Requires:	xtoolwait
# XFree86/X11 for xdpyinfo
Requires:	XFree86
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir %{_prefix}/lib

%description
Script that launches Mozilla or Firefox.

%description -l pl.UTF-8
Skrypt uruchiamiający Mozillę lub Firefoksa.

%prep
%setup -qcT
%{__bzip2} -dc %{SOURCE0} > %{name}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}
install %{name} $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*
