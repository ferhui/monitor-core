Summary: libe (a library of useful functions in C)
Name: libe
Version: 0.2.2
Release: 1
Copyright: GPL
Group: Development/Libraries
Source: libe-0.2.2.tar.gz

%description
libe (a library of useful functions in C)

%prep
%setup

%build
./configure --prefix=/usr
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
make install

%clean

%files
/usr/lib/libe.a
/usr/include/e/barrier.h
/usr/include/e/bitmask.h
/usr/include/e/bytes.h
/usr/include/e/cpa.h
/usr/include/e/e_error.h
/usr/include/e/hash.h 
/usr/include/e/io.h
/usr/include/e/net.h
/usr/include/e/safe.h
/usr/include/e/token_array.h
/usr/include/e/tree.h
/usr/include/e/xmalloc.h

%post 
