#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x8FE99503132D7742 (antonio@gnu.org)
#
Name     : plzip
Version  : 1.10
Release  : 7
URL      : https://download.savannah.gnu.org/releases/lzip/plzip/plzip-1.10.tar.gz
Source0  : https://download.savannah.gnu.org/releases/lzip/plzip/plzip-1.10.tar.gz
Source1  : https://download.savannah.gnu.org/releases/lzip/plzip/plzip-1.10.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: plzip-bin = %{version}-%{release}
Requires: plzip-info = %{version}-%{release}
Requires: plzip-license = %{version}-%{release}
Requires: plzip-man = %{version}-%{release}
BuildRequires : lzlib-dev

%description
Description
Plzip is a massively parallel (multi-threaded) implementation of lzip, fully
compatible with lzip 1.4 or newer. Plzip uses the compression library lzlib.

%package bin
Summary: bin components for the plzip package.
Group: Binaries
Requires: plzip-license = %{version}-%{release}

%description bin
bin components for the plzip package.


%package info
Summary: info components for the plzip package.
Group: Default

%description info
info components for the plzip package.


%package license
Summary: license components for the plzip package.
Group: Default

%description license
license components for the plzip package.


%package man
Summary: man components for the plzip package.
Group: Default

%description man
man components for the plzip package.


%prep
%setup -q -n plzip-1.10
cd %{_builddir}/plzip-1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643396602
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1643396602
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plzip
cp %{_builddir}/plzip-1.10/COPYING %{buildroot}/usr/share/package-licenses/plzip/244611d3ffa10dc67244ec317e7235aa5779f42a
%make_install
## install_append content
ln -s plzip %{buildroot}/usr/bin/lzip
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lzip
/usr/bin/plzip

%files info
%defattr(0644,root,root,0755)
/usr/share/info/plzip.info

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plzip/244611d3ffa10dc67244ec317e7235aa5779f42a

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/plzip.1
