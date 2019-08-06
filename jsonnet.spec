Name:    jsonnet
Version: 0.13.0
Release: 1%{?dist}
Summary: The data templating language

License: Apache-2.0
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Source0: https://github.com/google/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

Patch0: 0001-Properly-detect-a-system-GTest.patch
Patch1: 0002-Don-t-link-jsonnet-jsonnetfmt-statically.patch
Patch2: 0003-Update-VERSION-property.patch
Patch3: 0004-Fix-location-of-GNUInstallDirs-in-CMakeLists.txt.patch

%description
A data templating language for app and tool developers.

This package includes the jsonnet command-line tools.

%package libs
Summary: jsonnet runtime libraries

%description libs
This package includes the jsonnet runtime libraries.

%package devel
Summary: Headers for jsonnet development

%description devel
This package contains the headers for jsonnet development.

%prep
%setup -q

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
mkdir _build
cd _build
%cmake .. -DUSE_SYSTEM_GTEST=ON
%make_build

%install
cd _build
%make_install

%check
ctest -V %{?_smp_mflags}

%files
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt

%files libs
%{_libdir}/libjsonnet.so*

%files devel
%{_includedir}/libjsonnet.h
%{_includedir}/libjsonnet_fmt.h
%{_includedir}/libjsonnet++.h
