Summary:	SDL Graphics Extension
Summary(pl.UTF-8):	Rozszerzenie graficzne dla SDL
Name:		sge
Version:	020904
Release:	1
License:	LGPL
Group:		X11/Libraries
Source0:	http://home.swipnet.se/cal_home/sge/files/%{name}%{version}.tar.gz
# Source0-md5:	42e6c4b044cafa1858bbeb509166e0c6
#Patch0:		%{name}-rpmcflags.patch
#Patch1:		%{name}-sdl_image.patch
URL:		http://home.swipnet.se/cal_home/sge/
BuildRequires:	SDL_image-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGE is a high level graphics library for SDL.

%description -l pl.UTF-8
SGE jest wysokopoziomową biblioteką graficzną dla SDL.

%package devel
Summary:	Header files for SGE
Summary(pl.UTF-8):	Pliki nagłówkowe SGE
Group:		X11/Development/Libraries

%description devel
This packege contains header files for SGE library.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe biblioteki SGE.

%package static
Summary:	Files to link SGE applications statically
Summary(pl.UTF-8):	Pliki do statycznej konsolidacji aplikacji SGE
Group:		X11/Development/Libraries

%description static
This packege contains files necessary to link SGE applications
statically.

%description static -l pl.UTF-8
Ten pakiet zawiera pliki niezbędne do statycznej konsolidacji
aplikacji SGE.

%prep
%setup -q -n %{name}%{version}
#%patch0 -p1
#%patch1 -p1

%build
%{__make} shared \
	CFLAGS="%{rpmcflags} -Wall -ffast-math -fPIC \$(SGE_CFLAGS) \$(FT_CFLAGS)" \
	CXX="%{__cxx}" \
	LIBS="\$(SGE_LIBS) -Wl,-soname=libSGE.so.%{version}" \
	USE_IMG=y

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/sge,%{_examplesdir}/%{name}-%{version}}

install libSGE.so $RPM_BUILD_ROOT%{_libdir}/libSGE.so.%{version}
install libSGE.a $RPM_BUILD_ROOT%{_libdir}/libSGE.a
install *.h $RPM_BUILD_ROOT%{_includedir}/%{name}
ln -sf libSGE.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libSGE.so

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README Todo WhatsNew
%attr(755,root,root) %{_libdir}/*.so.*

%files devel
%defattr(644,root,root,755)
%doc docs/*
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/%{name}
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
