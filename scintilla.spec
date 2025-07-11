Summary:	Free source code editing component for GTK+ and Win32
Summary(pl.UTF-8):	Wolnodostępna kontrolka edycyjna dla GTK+ i Win32
Name:		scintilla
Version:	3.21.1
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	https://downloads.sourceforge.net/scintilla/%{name}%{fver}.tgz
# Source0-md5:	99ae337cb6e06a50cac099a6f1ec7100
Patch0:		%{name}-make.patch
Patch1:		%{name}-glib.patch
URL:		https://scintilla.org/
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	libstdc++-devel >= 6:4.8
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scintilla is a free source code editing component. It comes with
complete source code and a license that permits use in any free
project or commercial product. As well as features found in standard
text editing components, Scintilla includes features especially useful
when editing and debugging source code. These include support for
syntax styling, error indicators, code completion and call tips. The
selection margin can contain markers like those used in debuggers to
indicate breakpoints and the current line. Styling choices are more
open than with many editors, allowing the use of proportional fonts,
bold and italics, multiple foreground and background colours and
multiple fonts.

%description -l pl.UTF-8
Scintilla to wolnodostępna kontrolka do edycji kodu. Przychodzi z
pełnym kodem źródłowym i licencja pozwalającą na używanie w dowolnym
projekcie darmowym lub komercyjnym. Oprócz możliwości obecnych w
standardowych kontrolkach do edycji tekstu, Scintilla ma dodatkowe,
przydatne szczególnie przy edycji i szukaniu błędów w kodzie
źródłowym. Możliwości te obejmują obsługę stylu składni, podświetlanie
błędów, dopełnianie kodu i podpowiedzi. Marginesy mogą zawierać
znaczniki podobne do tych używanych do oznaczenia breakpointów lub
bieżącej linii w debuggerach. Wybór stylu jest bardziej otwarty niż w
wielu edytorach, pozwalając na użycie fontów proporcjonalnych,
pogrubionych i pochylonych, wielu kolorów pisma i tła oraz wielu
fontów.

%package devel
Summary:	scintilla header files
Summary(pl.UTF-8):	Pliki nagłówkowe scintilli
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.0
Requires:	libstdc++-devel >= 6:4.8

%description devel
scintilla header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe scintilli.

%package static
Summary:	Static scintilla library
Summary(pl.UTF-8):	Statyczna biblioteka scintilla
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static scintilla library.

%description static -l pl.UTF-8
Statyczna biblioteka scintilla.

%prep
%setup -q -n %{name}%{fver}
%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} -C gtk \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	GTK3=1 \
	OPTFLAGS="%{rpmcflags}" \
	libdir="%{_libdir}" \
	%{?debug:DEBUG=1}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/%{name}

%{__make} -C gtk install \
	libdir="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

cp -p include/*.h $RPM_BUILD_ROOT%{_includedir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt doc/*
%attr(755,root,root) %{_libdir}/libscintilla.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libscintilla.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libscintilla.so
%{_libdir}/libscintilla.la
%{_includedir}/scintilla

%files static
%defattr(644,root,root,755)
%{_libdir}/libscintilla.a
