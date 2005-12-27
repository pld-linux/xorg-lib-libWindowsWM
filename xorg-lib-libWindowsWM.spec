Summary:	WindowsWM extension library
Summary(pl):	Biblioteka rozszerzenia WindowsWM
Name:		xorg-lib-libWindowsWM
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/lib/libWindowsWM-%{version}.tar.bz2
# Source0-md5:	337b379fd00a67345b083100c4e6ba95
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-windowswmproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WindowsWM extension library.

%description -l pl
Biblioteka rozszerzenia WindowsWM.

%package devel
Summary:	Header files for WindowsWM library
Summary(pl):	Pliki nag³ówkowe biblioteki WindowsWM
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-windowswmproto-devel

%description devel
WindowsWM extension library.

This package contains the header files needed to develop programs that
use libWindowsWM.

%description devel -l pl
Biblioteka rozszerzenia WindowsWM.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libWindowsWM.

%package static
Summary:	Static WindowsWM library
Summary(pl):	Biblioteka statyczna WindowsWM
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
WindowsWM extension library.

This package contains the static libWindowsWM library.

%description static -l pl
Biblioteka rozszerzenia WindowsWM.

Pakiet zawiera statyczn± bibliotekê libWindowsWM.

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
%doc AUTHORS COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libWindowsWM.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libWindowsWM.so
%{_libdir}/libWindowsWM.la
%{_pkgconfigdir}/windowswm.pc
%{_mandir}/man3/WindowsWM.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libWindowsWM.a
