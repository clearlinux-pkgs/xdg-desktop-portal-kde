#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : xdg-desktop-portal-kde
Version  : 5.17.5
Release  : 39
URL      : https://download.kde.org/stable/plasma/5.17.5/xdg-desktop-portal-kde-5.17.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.17.5/xdg-desktop-portal-kde-5.17.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.17.5/xdg-desktop-portal-kde-5.17.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: xdg-desktop-portal-kde-data = %{version}-%{release}
Requires: xdg-desktop-portal-kde-license = %{version}-%{release}
Requires: xdg-desktop-portal-kde-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cups-dev
BuildRequires : kwayland-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(epoxy)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(libpipewire-0.2)
BuildRequires : util-linux

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
%setup -q -n xdg-desktop-portal-kde-5.17.5
cd %{_builddir}/xdg-desktop-portal-kde-5.17.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1579200131
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1579200131
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde
cp %{_builddir}/xdg-desktop-portal-kde-5.17.5/COPYING %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd clr-build
%make_install
popd
%find_lang xdg-desktop-portal-kde

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/xdg-desktop-portal-kde

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.freedesktop.impl.portal.desktop.kde.desktop
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
/usr/share/xdg-desktop-portal/portals/kde.portal

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-desktop-portal-kde/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files locales -f xdg-desktop-portal-kde.lang
%defattr(-,root,root,-)

