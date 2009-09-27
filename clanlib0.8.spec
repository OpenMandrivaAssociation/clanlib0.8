%define	name	clanlib0.8
%define	version	0.8.1
%define release %mkrel 5
%define	lib_name_orig libclanlib
%define	lib_major 0.8
%define	lib_name %mklibname clanlib %{lib_major}

# disable no_undefined, otherwise it fails on linking src
%define _disable_ld_no_undefined 1
Name:		%{name}
Summary:	The ClanLib Game SDK
Version:	%{version}
Release:	%{release}
License:	BSD-like
Group:		System/Libraries
Source0:	http://www.clanlib.org/download/releases-%{lib_major}/ClanLib-%version.tgz
Patch0:		clanlib-0.8.1-gcc43.patch
Patch1:		clanlib-0.8.1-ndebug.patch
Patch2:		clanlib-0.8.1-gcc44.patch
URL:		http://www.clanlib.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libhermes-devel >= 1.3.0 libmikmod-devel libpng-devel Mesa-common-devel autoconf2.5
BuildRequires:	libtiff-devel X11-static-devel bzip2-devel oggvorbis-devel DirectFB-devel
BuildRequires:  libSDL_gfx-devel
BuildRequires:  libxslt-proc

Obsoletes:	ClanLib
Provides:	ClanLib = %{version}-%{release}

%description
The ClanLib Game SDK is a crossplatform game library designed to ease the work
for game developers. The goal is to provide a common interface to classical
game problems (loading graphics eg.), so games can share as much code as
possible. Ideally anyone with small resources should be able to write
commercial quality games.

%package -n	%{lib_name}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{lib_name}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}-%{release}
Requires:	%{lib_name}-gl = %{version}-%{release}
Requires:	%{lib_name}-gui = %{version}-%{release}
Requires:	%{lib_name}-mikmod = %{version}-%{release}
Requires:	%{lib_name}-network = %{version}-%{release}
Requires:	%{lib_name}-sound = %{version}-%{release}
Requires:	%{lib_name}-vorbis = %{version}-%{release}
Requires:	%{lib_name}-sdl = %{version}-%{release}
Requires:	%{lib_name}-signals = %{version}-%{release}
Requires:	%{lib_name}-guistylesilver = %{version}-%{release}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Obsoletes:	ClanLib-devel clanlib-devel
Provides:	ClanLib-devel = %{version}-%{release} clanlib-devel = %{version}-%{release} %{name}-devel
Conflicts:	clanlib0.6-devel

%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{lib_name}-static-devel
Summary:	Static libraries for %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Obsoletes:	ClanLib-static-devel clanlib-static-devel
Provides:	ClanLib-static-devel = %{version}-%{release} clanlib-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
This package contains the static libraries for %{name}.

%package -n	%{lib_name}-sound
Summary:	ClanLib Sound module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-sound

%description -n	%{lib_name}-sound
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Sound module (clanSound).

%package -n	%{lib_name}-vorbis
Summary:	ClanLib Vorbis module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-vorbis

%description -n	%{lib_name}-vorbis
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Vorbis module (clanVorbis).

%package -n	%{lib_name}-network
Summary:	ClanLib Network module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-network

%description -n	%{lib_name}-network
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Network module (clanNetwork).

%package -n	%{lib_name}-gui
Summary:	ClanLib Gui module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gui

%description -n	%{lib_name}-gui
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Gui module (clanGUI).

%package -n	%{lib_name}-gl
Summary:	ClanLib GL module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gl

%description -n	%{lib_name}-gl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GL module (clanGL).

%package -n	%{lib_name}-mikmod
Summary:	ClanLib MikMod module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-mikmod clanlib-mikmod
Provides:	ClanLib-mikmod = %{version}-%{release} clanlib-mikmod = %{version}-%{release}
Provides:	%{lib_name_orig}-mikmod

%description -n	%{lib_name}-mikmod
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the MikMod module (clanMikMod).

%package -n	%{lib_name}-sdl
Summary:	ClanLib SDL module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-sdl clanlib-sdl
Provides:	ClanLib-sdl = %{version}-%{release} clanlib-sdl = %{version}-%{release}
Provides:	%{lib_name_orig}-sdl

%description -n	%{lib_name}-sdl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the SDL module (clanSDL).

%package -n	%{lib_name}-signals
Summary:	ClanLib Signals module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-png clanlib-signals
Provides:	ClanLib-png = %{version}-%{release} clanlib-signals = %{version}-%{release}
Provides:	%{lib_name_orig}-signals

%description -n	%{lib_name}-signals
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Signals module (clanSignals).

%package -n	%{lib_name}-guistylesilver
Summary:	ClanLib GUIStyleSilver module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Obsoletes:	ClanLib-png clanlib-guistylesilver
Provides:	ClanLib-png = %{version}-%{release} clanlib-guistylesilver = %{version}-%{release}
Provides:	%{lib_name_orig}-guistylesilver

%description -n	%{lib_name}-guistylesilver
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GUIStyleSilver module
(clanGUIStyleSilver).

%package	docs
Summary:	ClanLib documentation
Group:		Books/Computer books
Obsoletes:	ClanLib-docs clanlib-docs
Provides:	ClanLib-docs = %{version}-%{release} clanlib-docs = %{version}-%{release}

%description	docs
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package contains the documentation.

%prep
%setup -q -n ClanLib-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure2_5x	--enable-dyn \
		--enable-joystick \
		--disable-lua \
		--disable-debug \
		--with-pic \
		--enable-docs \
		--enable-ttf \
		--enable-clanDisplay \
		--enable-clanSDL \
		--enable-clanGL \
		--enable-clanSound \
		--enable-clanNetwork \
		--enable-clanGUI \
		--enable-clanMikMod \
		--enable-clanVorbis \
%ifarch %{ix86}
		--enable-asm386
%endif

%make all

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall BIN_PREFIX=$RPM_BUILD_ROOT%{_bindir} LIB_PREFIX=$RPM_BUILD_ROOT%{_libdir} INC_PREFIX=$RPM_BUILD_ROOT%{_includedir} TARGET_PREFIX=$RPM_BUILD_ROOT%{_libdir}/ClanLib
#make MAN_PREFIX=$RPM_BUILD_ROOT%{_mandir} HTML_PREFIX=$RPM_BUILD_ROOT%{_datadir}/doc/%{name}-docs-%{version}/Docs docs_install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la
ln -s ClanLib-0.7 $RPM_BUILD_ROOT%{_includedir}/ClanLib

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-mikmod -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-sound -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-vorbis -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-network -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-gui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-gl -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-sdl -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-signals -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%post -n %{lib_name}-guistylesilver -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun	-n %{lib_name}-mikmod -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-sound -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-vorbis -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-network -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-gui -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-gl -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-sdl -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-signals -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name}-guistylesilver -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{lib_name}
%defattr(-, root, root)
%doc README COPYING CREDITS
%{_libdir}/libclanCore-%{lib_major}.so.*
%{_libdir}/libclanApp-%{lib_major}.so.*
%{_libdir}/libclanDisplay-%{lib_major}.so.*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%doc README COPYING CODING_STYLE ascii-logo
%{_libdir}/*.so
%{_includedir}/ClanLib-%{lib_major}
%{_includedir}/ClanLib
#%{_bindir}/clanlib-config
%{_libdir}/pkgconfig/*.pc

%files -n %{lib_name}-static-devel
%defattr(-, root, root)
%{_libdir}/*.a

%files docs
%defattr(-, root, root)
%{_docdir}/clanlib

%files -n %{lib_name}-mikmod
%defattr(-, root, root)
%{_libdir}/libclanMikMod-%{lib_major}.so.*

%files -n %{lib_name}-network
%defattr(-, root, root)
%{_libdir}/libclanNetwork-%{lib_major}.so.*

%files -n %{lib_name}-vorbis
%defattr(-, root, root)
%{_libdir}/libclanVorbis-%{lib_major}.so.*

%files -n %{lib_name}-sound
%defattr(-, root, root)
%{_libdir}/libclanSound-%{lib_major}.so.*

%files -n %{lib_name}-gui
%defattr(-, root, root)
%{_libdir}/libclanGUI-%{lib_major}.so.*

%files -n %{lib_name}-gl
%defattr(-, root, root)
%{_libdir}/libclanGL-%{lib_major}.so.*

%files -n %{lib_name}-sdl
%defattr(-, root, root)
%{_libdir}/libclanSDL-%{lib_major}.so.*

%files -n %{lib_name}-signals
%defattr(-, root, root)
%{_libdir}/libclanSignals-%{lib_major}.so.*

%files -n %{lib_name}-guistylesilver
%defattr(-, root, root)
%{_libdir}/libclanGUIStyleSilver-%{lib_major}.so.*



