Summary:	Free source code editing component for Win32 and GTK+
Summary(pl):	-
Name:		scintilla
Version:	1.53
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://dl.sf.net/scintilla/scintilla153.tgz
# Source0-md5:	fd83f5efeb0084bd68fe30116489637f
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
