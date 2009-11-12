Summary:	WindowsWM extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia WindowsWM
Name:		xorg-lib-libWindowsWM
Version:	1.0.1
Release:	2
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2
# Source0-md5:	274b2b5620a524fd7bb739edb97317f5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-windowswmproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WindowsWM is a simple library designed to interface with the
Windows-WM extension. This extension allows X window managers to
better interact with the Cygwin XWin server when running X11 in a
rootless mode.

%description -l pl.UTF-8
WindowsWM to prosta biblioteka zaprojektowana jako interfejs do
rozszerzenia Windows-WM. Rozszerzenie to pozwala zarządcom okien X
lepiej współpracować z cygwinowym serwerem XWin, kiedy X11 działa w
trybie "rootless".

%package devel
Summary:	Header files for WindowsWM library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki WindowsWM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-windowswmproto-devel

%description devel
WindowsWM extension library.

This package contains the header files needed to develop programs that
use libWindowsWM.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia WindowsWM.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libWindowsWM.

%package static
Summary:	Static WindowsWM library
Summary(pl.UTF-8):	Biblioteka statyczna WindowsWM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
WindowsWM extension library.

This package contains the static libWindowsWM library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia WindowsWM.

Pakiet zawiera statyczną bibliotekę libWindowsWM.

%prep
%setup -q -n libWindowsWM-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libWindowsWM.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libWindowsWM.so.7

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWindowsWM.so
%{_libdir}/libWindowsWM.la
%{_pkgconfigdir}/windowswm.pc
%{_mandir}/man3/WindowsWM.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libWindowsWM.a
