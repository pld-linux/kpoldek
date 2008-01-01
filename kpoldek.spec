Summary:	Kpoldek - Qt4-based GUI for poldek
Summary(pl.UTF-8):	Kpoldek - graficzny interfejs do poldka oparty na Qt4
Name:		kpoldek
Version:	0.01alpha
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://kde-apps.org/CONTENT/content-files/53979-%{name}.tar.gz
# Source0-md5:	9698f2725876a2babc61ef13b90fbcf0
URL:		http://kde-apps.org/content/show.php?content=53979
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	poldek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a small program to manage a RPM packages using external
application like poldek. Actually it is just an graphic interface, so
don't blame me. I think it might be useful for people, that are lazy
to do this command things.

%description -l pl.UTF-8
Ten program służy do zarządzania pakietami RPM przy użyciu zewnętrznej
aplikacji jaką jest poldek. Właściwie jest to tylko graficzny
interfejs. Autor ma nadzieję, że będzie przydatny dla ludzi zbyt
leniwych by wydawać polecenia ręcznie.

%prep
%setup -q -n %{name}

%build
rm -f src/Makefile
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bin/kpoldek $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpoldek
