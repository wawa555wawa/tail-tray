%global app_version %{?version}%{!?version:0.2.36}

Name:           tail-tray
Version:        %{app_version}
Release:        1%{?dist}
Summary:        Tailscale tray application for Linux desktops

License:        GPL-3.0-or-later
URL:            https://github.com/SneWs/tail-tray
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-knotifications-devel

Requires:       tailscale
Recommends:     davfs2

%description
Tail Tray provides a system tray application and UI for Tailscale on Linux.

%description -l zh_CN
Tail Tray 为 Linux 桌面提供 Tailscale 的系统托盘应用和图形界面，
支持账户管理、出口节点、子网路由、Tail Drive 文件共享、Tail Drop
文件传输以及可脚本化操作等功能，界面支持简体中文。

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DKNOTIFICATIONS_ENABLED=ON \
    -DBUILD_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_bindir}/tail-tray
%{_datadir}/applications/tail-tray.desktop
%{_datadir}/knotifications6/tail-tray.notifyrc
%{_datadir}/icons/hicolor/scalable/apps/tail-tray-dark.svg
%{_datadir}/icons/hicolor/scalable/apps/tail-tray.svg
%{_libdir}/tail-tray/*.qm

%changelog
* Sun Oct 04 2026 Tail Tray packaging <packaging@localhost> - %{version}-1
- Add Simplified Chinese (zh_CN) translation
- Install translation catalogs, they were previously not packaged

* Wed Jul 29 2026 Marcus Grenangen <marcus@grenangen.se> - %{version}-1
- Add Fedora RPM spec for GitHub CI builds


