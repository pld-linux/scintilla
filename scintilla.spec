Summary:	-
Summary(pl):	-
Name:		scintilla
Version:	1.53
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://scintilla.org/scintilla153.tgz
URL:		http://scintilla.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}

%build
%{__make} -C gtk

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
