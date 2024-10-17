%define	lib_name_orig	libclanlib
%define	lib_major	0.8
%define	lib_name	%mklibname clanlib %{lib_major}

Name:		clanlib0.8
Summary:	The ClanLib Game SDK
Version:	0.8.1
Release:	8
License:	BSD-like
Group:		System/Libraries
URL:		https://www.clanlib.org/
Source0:	http://www.clanlib.org/download/releases-%{lib_major}/ClanLib-%version.tgz
Patch0:		clanlib-0.8.1-gcc43.patch
Patch1:		clanlib-0.8.1-ndebug.patch
Patch2:		clanlib-0.8.1-gcc44.patch
Patch3:		clanlib-0.8.1-libpng1.5.patch
Patch4:		clanlib-0.8.1-link.patch
Patch5:		ClanLib-0.8.1-gcc4.7.patch
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	libmikmod-devel
BuildRequires:	jpeg-devel
BuildRequires:	libxslt-proc

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
Provides:	%{name}-devel
Conflicts:	clanlib0.6-devel

%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	%{lib_name}-static-devel
Summary:	Static libraries for %{name}
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-static-devel = %{version}-%{release}
Provides:	%{name}-static-devel = %{version}-%{release}

%description -n	%{lib_name}-static-devel
This package contains the static libraries for %{name}.

%package -n	%{lib_name}-sound
Summary:	ClanLib Sound module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-sound = %{version}-%{release}

%description -n	%{lib_name}-sound
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Sound module (clanSound).

%package -n	%{lib_name}-vorbis
Summary:	ClanLib Vorbis module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-vorbis = %{version}-%{release}

%description -n	%{lib_name}-vorbis
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Vorbis module (clanVorbis).

%package -n	%{lib_name}-network
Summary:	ClanLib Network module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-network = %{version}-%{release}

%description -n	%{lib_name}-network
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Network module (clanNetwork).

%package -n	%{lib_name}-gui
Summary:	ClanLib Gui module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gui = %{version}-%{release}

%description -n	%{lib_name}-gui
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Gui module (clanGUI).

%package -n	%{lib_name}-gl
Summary:	ClanLib GL module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-gl = %{version}-%{release}

%description -n	%{lib_name}-gl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GL module (clanGL).

%package -n	%{lib_name}-mikmod
Summary:	ClanLib MikMod module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-mikmod = %{version}-%{release}

%description -n	%{lib_name}-mikmod
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the MikMod module (clanMikMod).

%package -n	%{lib_name}-sdl
Summary:	ClanLib SDL module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-sdl = %{version}-%{release}

%description -n	%{lib_name}-sdl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the SDL module (clanSDL).

%package -n	%{lib_name}-signals
Summary:	ClanLib Signals module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-signals = %{version}-%{release}

%description -n	%{lib_name}-signals
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Signals module (clanSignals).

%package -n	%{lib_name}-guistylesilver
Summary:	ClanLib GUIStyleSilver module
Group:		System/Libraries
Requires:	%{lib_name} = %{version}-%{release}
Provides:	%{lib_name_orig}-guistylesilver = %{version}-%{release}

%description -n	%{lib_name}-guistylesilver
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GUIStyleSilver module
(clanGUIStyleSilver).

%package	docs
Summary:	ClanLib documentation
Group:		Books/Computer books

%description	docs
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package contains the documentation.

%prep
%setup -q -n ClanLib-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1

%build
./autogen.sh
# disable no_undefined, otherwise it fails on linking src
%define _disable_ld_no_undefined 1
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
%makeinstall BIN_PREFIX=%{buildroot}%{_bindir} LIB_PREFIX=%{buildroot}%{_libdir} INC_PREFIX=%{buildroot}%{_includedir} TARGET_PREFIX=%{buildroot}%{_libdir}/ClanLib

ln -s ClanLib-0.7 %{buildroot}%{_includedir}/ClanLib

%files -n %{lib_name}
%doc README COPYING CREDITS
%{_libdir}/libclanCore-%{lib_major}.so.*
%{_libdir}/libclanApp-%{lib_major}.so.*
%{_libdir}/libclanDisplay-%{lib_major}.so.*

%files -n %{lib_name}-devel
%doc README COPYING CODING_STYLE ascii-logo
%{_libdir}/*.so
%{_includedir}/ClanLib-%{lib_major}
%{_includedir}/ClanLib
#{_bindir}/clanlib-config
%{_libdir}/pkgconfig/*.pc

%files -n %{lib_name}-static-devel
%{_libdir}/*.a

%files docs
%{_docdir}/clanlib

%files -n %{lib_name}-mikmod
%{_libdir}/libclanMikMod-%{lib_major}.so.*

%files -n %{lib_name}-network
%{_libdir}/libclanNetwork-%{lib_major}.so.*

%files -n %{lib_name}-vorbis
%{_libdir}/libclanVorbis-%{lib_major}.so.*

%files -n %{lib_name}-sound
%{_libdir}/libclanSound-%{lib_major}.so.*

%files -n %{lib_name}-gui
%{_libdir}/libclanGUI-%{lib_major}.so.*

%files -n %{lib_name}-gl
%{_libdir}/libclanGL-%{lib_major}.so.*

%files -n %{lib_name}-sdl
%{_libdir}/libclanSDL-%{lib_major}.so.*

%files -n %{lib_name}-signals
%{_libdir}/libclanSignals-%{lib_major}.so.*

%files -n %{lib_name}-guistylesilver
%{_libdir}/libclanGUIStyleSilver-%{lib_major}.so.*

