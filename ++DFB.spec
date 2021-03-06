# NOTE: for version >= 1.7.0+ see -c++-* subpackages in DirectFB.spec
Summary:	Advanced version of C++ binding for DirectFB
Summary(pl.UTF-8):	Zaawansowana wersja interfejsu C++ do DirectFB
Name:		++DFB
Version:	1.4.2
Release:	1.1
License:	LGPL v2+
Group:		Libraries
Source0:	http://www.directfb.org/downloads/Extras/%{name}-%{version}.tar.gz
# Source0-md5:	7f2672b391d9987f16a0768e87f12306
URL:		http://www.directfb.org/index.php?path=Projects%2F%2B%2BDFB
BuildRequires:	DirectFB-devel >= 1:%{version}
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
Provides:	__DFB = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
++DFB is an advanced version of DFB++. It's an incompatible fork
with fundamental changes.

Applications no longer deal with interface pointers. The classes
wrapping around interfaces are used as container for an interface
pointer, providing garbage collection the "direct" way 8-)

%description -l pl.UTF-8
++DFB to zaawansowana wersja DFB++. Jest to niekompatybilne
odgałęzienie z zasadniczymi zmianami.

Aplikacje nie zajmują się już wskaźnikami do interfejsów. Klasy
obudowujące interfejsy są używane jako kontenery dla wskaźnika na
interfejs, udostępniając odśmiecanie w "bezpośredni" sposób.

%package devel
Summary:	++DFB header files
Summary(pl.UTF-8):	Pliki nagłówkowe ++DFB
Group:		Development/Libraries
# rpm can't stand cap beginning with '+'
#Requires:	%{name} = %{version}-%{release}
Requires:	__DFB = %{version}-%{release}
Requires:	DirectFB-devel >= 1:%{version}
Requires:	libstdc++-devel
Provides:	__DFB-devel = %{version}-%{release}

%description devel
Header files for ++DFB library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki ++DFB.

%package static
Summary:	++DFB static library
Summary(pl.UTF-8):	Statyczna biblioteka ++DFB
Group:		Development/Libraries
# rpm can't stand cap beginning with '+'
#Requires:	%{name}-devel = %{version}-%{release}
Requires:	__DFB-devel = %{version}-%{release}

%description static
++DFB static library.

%description static -l pl.UTF-8
Statyczna biblioteka ++DFB.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/simple.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/dfbplay
# not needed, conflict with DFB++
#%attr(755,root,root) %{_bindir}/dfbshow
#%attr(755,root,root) %{_bindir}/dfbswitch
%attr(755,root,root) %{_libdir}/lib++dfb-1.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib++dfb-1.4.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/++dfb-config
%attr(755,root,root) %{_libdir}/lib++dfb.so
%{_libdir}/lib++dfb.la
%{_includedir}/++dfb
%{_pkgconfigdir}/++dfb.pc
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/lib++dfb.a
