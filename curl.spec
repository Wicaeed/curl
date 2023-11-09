Name:		curl
Version:	8.4.0
Release:	1%{?dist}
Summary:	An updated & repackaged CURL binary

Group:		Networking/Utilities
License:	MIT License
URL:		https://curl.haxx.se
Source0: 	%{name}-%{version}.tar.gz

BuildRequires:	openssl-devel
Requires:	libcurl

%description
A repackaged/updated curl binary for CentOS 7 hosts that contains the fixes for CVE-2023-38545 & others

%prep
%setup -q

%build
./configure \
	--prefix=/usr \
	--with-zstd \
	--with-openssl \
	--with-libidn2 \
	--without-brotli \
	--without-nghttp2 \
	--without-sasl \
	--without-zstd \
	--without-libpsl \
	--without-libgsasl \
	--disable-proxy \
	--disable-alt-svc \
	--disable-ntlm-wb
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install %{name} DESTDIR=%{buildroot}
libtool --finish /usr/lib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/usr/bin/curl
/usr/bin/curl-config
/usr/include/curl/*.h
/usr/lib/libcurl.*
/usr/lib/pkgconfig/libcurl.pc
/usr/share/aclocal/libcurl.m4
/usr/share/man/man1/*.gz
/usr/share/man/man3/*.gz

make install DESTDIR=%{buildroot}

#%doc

%changelog