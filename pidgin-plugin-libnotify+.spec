%define		short_name	pidgin-libnotify+
Summary:	Provides libnotify interface to Pidgin
Summary(pl.UTF-8):	Dostarcza interfejs libnotify dla Pidgina
Name:		pidgin-plugin-libnotify+
Version:	1.2.2
Release:	4
License:	GPL v3+
Group:		Applications
Source0:	https://github.com/downloads/sardemff7/Pidgin-Libnotify-plus/pidgin-libnotify-plus-%{version}.tar.xz
# Source0-md5:	8688623b47ad1117f682dc1d13894937
URL:		https://github.com/sardemff7/Pidgin-Libnotify-plus/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pidgin-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides libnotify interface to Pidgin.

%description -l pl.UTF-8
Dostarcza interfejs libnotify dla Pidgina.

%prep
%setup -q -n %{short_name}-%{version}

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/pidgin/pidgin-libnotify+.la

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/pidgin/pidgin-libnotify+.so
