#
# Conditional build:
# _with_gtk1	- use GTK+ 1.2 instead of 2.0
#
Summary:	Free source code editing component for GTK+ and Win32
Summary(pl):	Wolnodostêpna kontrolka edycyjna dla GTK+ i Win32
Name:		scintilla
Version:	1.53
Release:	1
License:	BSD-like
Group:		Libraries
# Source0-md5:	fd83f5efeb0084bd68fe30116489637f
Source0:	http://dl.sf.net/scintilla/scintilla153.tgz
Patch0:		%{name}-make.patch
URL:		http://scintilla.org/
%{?_with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?_with_gtk1:BuildRequires:	gtk+2-devel >= 2.0.0}
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scintilla is a free source code editing component. It comes with
complete source code and a license that permits use in any free
project or commercial product. As well as features found in standard
text editing components, Scintilla includes features especially useful
when editing and debugging source code. These include support for syntax
styling, error indicators, code completion and call tips. The selection
margin can contain markers like those used in debuggers to indicate
breakpoints and the current line. Styling choices are more open than with
many editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%description -l pl
Scintilla to wolnodostêpna kontrolka do edycji kodu. Przychodzi z
pe³nym kodem ¼ród³owym i licencja pozwalaj±c± na u¿ywanie w dowolnym
projekcie darmowym lub komercyjnym. Oprócz mo¿liwo¶ci obecnych w
standardowych kontrolkach do edycji tekstu, Scintilla ma dodatkowe,
przydatne szczególnie przy edycji i szukaniu b³êdów w kodzie
¼ród³owym. Mo¿liwo¶ci te obejmuj± obs³ugê stylu sk³adni, pod¶wietlanie
b³êdów, dope³nianie kodu i podpowiedzi. Marginesy mog± zawieraæ
znaczniki podobne do tych u¿ywanych do oznaczenia breakpointów lub
bie¿±cej linii w debuggerach. Wybór stylu jest bardziej otwarty ni¿ w
wielu edytorach, pozwalaj±c na u¿ycie fontów proporcjonalnych,
pogrubionych i pochylonych, wielu kolorów pisma i t³a oraz wielu
fontów.

%package devel
Summary:	scintilla header files
Summary(pl):	Pliki nag³ówkowe scintilli
Group:		Development/Libraries
Requires:	%{name} = %{version}
%{?_with_gtk1:Requires:	gtk+-devel >= 1.2.0}
%{!?_with_gtk1:Requires:	gtk+2-devel >= 2.0.0}

%description devel
scintilla header files.

%description devel -l pl
Pliki nag³ówkowe scintilli.

%package static
Summary:	Static scintilla library
Summary(pl):	Statyczna biblioteka scintilla
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static scintilla library.

%description static -l pl
Statyczna biblioteka scintilla.

%prep
%setup -q -n %{name}
%patch -p1

%build
%{__make} -C gtk \
	CC="%{__cxx}" \
	OPTFLAGS="%{rpmcflags}" \
	%{?debug:DEBUG=1} \
	%{!?_with_gtk1:GTK2=1}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C gtk install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}/scintilla
install include/*.h $RPM_BUILD_ROOT%{_includedir}/scintilla

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc License.txt doc/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/scintilla

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
