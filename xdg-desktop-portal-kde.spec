#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : xdg-desktop-portal-kde
Version  : 5.13.5
Release  : 4
URL      : https://download.kde.org/stable/plasma/5.13.5/xdg-desktop-portal-kde-5.13.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.13.5/xdg-desktop-portal-kde-5.13.5.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.13.5/xdg-desktop-portal-kde-5.13.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-kde-data
Requires: xdg-desktop-portal-kde-license
Requires: xdg-desktop-portal-kde-locales
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kwayland-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libpipewire-0.2)

%description
# xdg-desktop-portal-kde
A backend implementation for [xdg-desktop-portal](http://github.com/flatpak/xdg-desktop-portal)
that is using Qt/KF5.

%package data
Summary: data components for the xdg-desktop-portal-kde package.
Group: Data

%description data
data components for the xdg-desktop-portal-kde package.


%package license
Summary: license components for the xdg-desktop-portal-kde package.
Group: Default

%description license
license components for the xdg-desktop-portal-kde package.


%package locales
Summary: locales components for the xdg-desktop-portal-kde package.
Group: Default

%description locales
locales components for the xdg-desktop-portal-kde package.


%prep
%setup -q -n xdg-desktop-portal-kde-5.13.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536125201
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1536125201
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/xdg-desktop-portal-kde
cp COPYING %{buildroot}/usr/share/doc/xdg-desktop-portal-kde/COPYING
pushd clr-build
%make_install
popd
%find_lang xdg-desktop-portal-kde

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/xdg-desktop-portal-kde

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
/usr/share/xdg-desktop-portal/portals/kde.portal

%files license
%defattr(-,root,root,-)
/usr/share/doc/xdg-desktop-portal-kde/COPYING

%files locales -f xdg-desktop-portal-kde.lang
%defattr(-,root,root,-)

