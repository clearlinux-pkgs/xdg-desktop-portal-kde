#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : xdg-desktop-portal-kde
Version  : 6.3.5
Release  : 117
URL      : https://download.kde.org/stable/plasma/6.3.5/xdg-desktop-portal-kde-6.3.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.3.5/xdg-desktop-portal-kde-6.3.5.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.3.5/xdg-desktop-portal-kde-6.3.5.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: xdg-desktop-portal-kde-data = %{version}-%{release}
Requires: xdg-desktop-portal-kde-license = %{version}-%{release}
Requires: xdg-desktop-portal-kde-locales = %{version}-%{release}
Requires: xdg-desktop-portal-kde-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cups-dev
BuildRequires : extra-cmake-modules
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : kirigami2-dev
BuildRequires : knotifications-dev
BuildRequires : kservice-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : kwayland-dev
BuildRequires : pipewire-dev
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
BuildRequires : wayland-protocols-dev plasma-wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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


%package services
Summary: services components for the xdg-desktop-portal-kde package.
Group: Systemd services
Requires: systemd

%description services
services components for the xdg-desktop-portal-kde package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n xdg-desktop-portal-kde-6.3.5
cd %{_builddir}/xdg-desktop-portal-kde-6.3.5
pushd ..
cp -a xdg-desktop-portal-kde-6.3.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747167880
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747167880
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/a4c60b3fefda228cd7439d3565df043192fef137 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/19d98e1b6f8ef12849ea4012a052d3907f336c91 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/xdg-desktop-portal-kde-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/xdg-desktop-portal-kde/adadb67a9875aeeac285309f1eab6e47d9ee08a7 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang xdg-desktop-portal-kde
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/V3/usr/lib64/libexec/xdg-desktop-portal-kde
/usr/lib64/libexec/xdg-desktop-portal-kde

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.freedesktop.impl.portal.desktop.kde.desktop
/usr/share/dbus-1/services/org.freedesktop.impl.portal.desktop.kde.service
/usr/share/knotifications6/xdg-desktop-portal-kde.notifyrc
/usr/share/qlogging-categories6/xdp-kde.categories
/usr/share/xdg-desktop-portal/portals/kde.portal

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xdg-desktop-portal-kde/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/xdg-desktop-portal-kde/19d98e1b6f8ef12849ea4012a052d3907f336c91
/usr/share/package-licenses/xdg-desktop-portal-kde/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/xdg-desktop-portal-kde/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/xdg-desktop-portal-kde/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/xdg-desktop-portal-kde/a4c60b3fefda228cd7439d3565df043192fef137
/usr/share/package-licenses/xdg-desktop-portal-kde/adadb67a9875aeeac285309f1eab6e47d9ee08a7
/usr/share/package-licenses/xdg-desktop-portal-kde/e458941548e0864907e654fa2e192844ae90fc32

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-xdg-desktop-portal-kde.service

%files locales -f xdg-desktop-portal-kde.lang
%defattr(-,root,root,-)

