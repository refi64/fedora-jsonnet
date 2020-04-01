Name:    jsonnet
Version: 0.15.0
Release: 1%{?dist}
Summary: The data templating language

License: Apache-2.0
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: json-devel
BuildRequires: make

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Source0: https://github.com/google/%{name}/archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz

%description
A data templating language for app and tool developers.

This package contains the jsonnet command-line tools.

%package libs
Summary: jsonnet runtime libraries

%description libs
This package contains the jsonnet runtime libraries.

%package c++
Summary: jsonnet C++ libraries

%description c++
Summary: This package contains jsonnet the C++ binding libraries.

%package devel
Summary: Headers for jsonnet development

%description devel
This package contains the headers for jsonnet development.

%package c++-devel
Summary: Headers for jsonnet C++ development

%description c++-devel
This package contains the headers for jsonnet C++ development.

%prep
%setup -q

%build
mkdir _build
cd _build
%cmake .. -DUSE_SYSTEM_GTEST=ON  -DUSE_SYSTEM_JSON=ON -DBUILD_SHARED_BINARIES=ON -DBUILD_STATIC_LIBS=OFF
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

%files c++
%{_libdir}/libjsonnet++.so*

%files devel
%{_includedir}/libjsonnet.h
%{_includedir}/libjsonnet_fmt.h

%files c++-devel
%{_includedir}/libjsonnet++.h
