Name: meego-panel-status
Summary: Status panel
Version: 0.2.5
Release: %mkrel 1
Group: System/Desktop
License: LGPL 2.1
URL: http://www.meego.com
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source/%{name}-%{version}.tar.gz
Patch0: meego-panel-status-0.2.5-champlain-version.patch
Patch1: meego-panel-status-0.2.5-fix-sources.patch
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
BuildRequires: libdbus-glib-devel
BuildRequires: mx-devel
BuildRequires: libGConf2-devel
Obsoletes: moblin-panel-status <= 0.0.10

%description
Meego status panel

%package devel
Summary: Status panel header files and development library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Description: Meego status panel

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf --install
%configure2_5x \
  --disable-static \
  --with-online=connman
make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang meego-panel-status

rm %{buildroot}%{_libdir}/libmeego-panel-status.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f meego-panel-status.lang
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/meego-panel-status
%{_datadir}/dbus-1/services/com.meego.UX.Shell.Panels.status.service
%{_datadir}/meego-panel-status/theme/add_status_header.png
%{_datadir}/meego-panel-status/theme/add_status_header_hover.png
%{_datadir}/meego-panel-status/theme/alt_status_header.png
%{_datadir}/meego-panel-status/theme/alt_status_header_hover.png
%{_datadir}/meego-panel-status/theme/avatar_frame.png
%{_datadir}/meego-panel-status/theme/avatar_icon.png
%{_datadir}/meego-panel-status/theme/content-panel-background.png
%{_datadir}/meego-panel-status/theme/current_status_header.png
%{_datadir}/meego-panel-status/theme/icon-bg-hover.png
%{_datadir}/meego-panel-status/theme/location-box-bg.png
%{_datadir}/meego-panel-status/theme/panel-background.png
%{_datadir}/meego-panel-status/theme/panel.css
%{_datadir}/meego-panel-status/theme/retweet-hover.png
%{_datadir}/meego-panel-status/theme/retweet.png
%{_datadir}/meego-panel-status/theme/status_card_background.png
%{_datadir}/meego-panel-status/theme/status_entry_box.png
%{_datadir}/meego-panel-status/theme/status_header_hover.png
%{_datadir}/meego-panel-status/theme/tweet-reply-hover.png
%{_datadir}/meego-panel-status/theme/tweet-reply.png
%{_datadir}/meego-panel-status/theme/background-gradient.png
%{_datadir}/meego-panel-status/theme/content-panel-header-grey.png
%{_datadir}/meego-panel-status/theme/people.png
%{_datadir}/mutter-meego/panels/meego-panel-status.desktop
%{_libdir}/libmeego-panel-status.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/libmeego-panel-status.so
%{_libdir}/pkgconfig/meego-panel-status.pc
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h

