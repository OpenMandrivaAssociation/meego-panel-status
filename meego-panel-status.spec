Name: meego-panel-status
Summary: Status panel for MeeGo
Group: Graphical desktop/Other 
Version: 0.2.5
License: LGPL 2.1
URL: http://www.meego.com
Release: %mkrel 1
Source: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Patch0: meego-panel-status-0.2.5-champlain-version.patch
Patch1: meego-panel-status-0.2.5-fix-sources.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
BuildRequires: meego-panel-devel
BuildRequires: libtelepathy-glib-devel
BuildRequires: clutter-gtk-devel
BuildRequires: libsocialweb-devel
BuildRequires: nbtk-devel
BuildRequires: libchamplain-devel
BuildRequires: libgeoclue-devel
Obsoletes: moblin-panel-status <= 0.0.10

%description
MeeGo status panel

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf --install
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}


%clean
rm -rf %{buildroot}

# TODO: -devel package

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING NEWS AUTHORS README ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
%{_libdir}/*
%{_includedir}/*
%{_datadir}/mutter-meego/*
