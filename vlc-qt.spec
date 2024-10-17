# Since version 1.0.0 there are new library names
%define	oname		VLCQt
%define	major		1.1
%define	libname			%mklibname %{name} %{major}
%define	develname		%mklibname %{name} -d
%define	oldlibname		%mklibname %{name} 0.10
%define	libnamewdt		%mklibname %{name}-widgets %{major}
%define	develnamewdt	%mklibname %{name}-widgets -d
%define	oldlibnamewdt	%mklibname %{name}-widgets 0.10
%define	libnameqml		%mklibname %{name}-qml %{major}
%define	develnameqml	%mklibname %{name}-qml -d
%define	oldlibnameqml	%mklibname %{name}-qml 0.10


Summary:	A simple library to connect Qt application with libvlc
Name:		vlc-qt
Version:	1.1.1
Release:	1
License:	GPLv3+
Group:		System/Libraries
Url:		https://projects.tano.si/library
Source:		https://github.com/vlc-qt/vlc-qt/archive/%{name}-%{version}.tar.gz
#Patch0:		vlc-qt-0.8.1-linkage.patch
# Also build pkgconfig files for QML and widgets libraries
#Patch1:		vlc-qt-0.8.1-pkgconfig.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(libvlc)
BuildRequires:  qmake5

%description
VLC-Qt is a free library used to connect Qt and libvlc libraries.
It contains core classes for main media playback and also some GUI
classes for faster media player developement.

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	A simple library to connect Qt applications with libvlc (core)
Group:		System/Libraries
Requires:	%{libname} = %{EVRD}
%rename		%{oldlibname}

%description -n %{libname}
VLC-Qt is a free library used to connect Qt and libvlc libraries.
It contains core classes for main media playback and also some GUI
classes for faster media player development.
This package contains the %{name} core library.

%files  -n %{libname}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/lib%{oname}Core.so.%{major}
%{_libdir}/lib%{oname}Core.so.%{major}.*

#----------------------------------------------------------------------------

%package -n	%{develname}
Summary:	Headers and development libraries for %{name} core library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{develname}
Headers and development libraries for %{name} core library.

%files  -n %{develname}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/cmake/%{oname}Core/*.cmake
%{_libdir}/pkgconfig/lib%{oname}Core.pc
%{_libdir}/lib%{oname}Core.so
%{_includedir}/%{oname}Core/AbstractVideoFrame.h
%{_includedir}/%{oname}Core/AbstractVideoStream.h
%{_includedir}/%{oname}Core/Audio.h
%{_includedir}/%{oname}Core/Common.h
%{_includedir}/%{oname}Core/Config.h
%{_includedir}/%{oname}Core/Enums.h
%{_includedir}/%{oname}Core/Equalizer.h
%{_includedir}/%{oname}Core/Error.h
%{_includedir}/%{oname}Core/Instance.h
%{_includedir}/%{oname}Core/Media.h
%{_includedir}/%{oname}Core/MediaList.h
%{_includedir}/%{oname}Core/MediaListPlayer.h
%{_includedir}/%{oname}Core/MediaPlayer.h
%{_includedir}/%{oname}Core/MetaManager.h
%{_includedir}/%{oname}Core/ModuleDescription.h
%{_includedir}/%{oname}Core/SharedExportCore.h
%{_includedir}/%{oname}Core/Stats.h
%{_includedir}/%{oname}Core/TrackModel.h
%{_includedir}/%{oname}Core/Video.h
%{_includedir}/%{oname}Core/VideoDelegate.h
%{_includedir}/%{oname}Core/VideoFrame.h
%{_includedir}/%{oname}Core/VideoMemoryStream.h
%{_includedir}/%{oname}Core/VideoStream.h
%{_includedir}/%{oname}Core/YUVVideoFrame.h

#----------------------------------------------------------------------------

%package -n	%{libnamewdt}
Summary:	A simple library to connect Qt application with libvlc (widgets)
Group:		System/Libraries
%rename		%{oldlibnamewdt}

%description -n %{libnamewdt}
VLC-Qt is a free library used to connect Qt and libvlc libraries.
It contains core classes for main media playback and also some GUI
classes for faster media player development.
This package contains the %{name}-widgets library.

%files  -n %{libnamewdt}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/lib%{oname}Widgets.so.%{major}
%{_libdir}/lib%{oname}Widgets.so.%{major}.*

#----------------------------------------------------------------------------

%package -n	%{develnamewdt}
Summary:	Headers and development libraries for %{name}-widgets library
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libnamewdt} = %{EVRD}
Requires:	%{develname} = %{EVRD}
Provides:	%{name}-widgets-devel = %{EVRD}

%description -n %{develnamewdt}
Headers and development libraries for %{name}-widgets library.

%files  -n %{develnamewdt}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/cmake/%{oname}Widgets/*.cmake
%{_libdir}/pkgconfig/lib%{oname}Widgets.pc
%{_libdir}/lib%{oname}Widgets.so
%{_includedir}/%{oname}Widgets/ControlAudio.h
%{_includedir}/%{oname}Widgets/ControlVideo.h
%{_includedir}/%{oname}Widgets/SharedExportWidgets.h
%{_includedir}/%{oname}Widgets/WidgetSeek.h
%{_includedir}/%{oname}Widgets/WidgetSeekProgress.h
%{_includedir}/%{oname}Widgets/WidgetVideo.h
%{_includedir}/%{oname}Widgets/WidgetVolumeSlider.h

#----------------------------------------------------------------------------

%package -n	%{libnameqml}
Summary:	A simple library to connect Qt application with libvlc (qml)
Group:		System/Libraries
%rename		%{oldlibnameqml}

%description -n %{libnameqml}
VLC-Qt is a free library used to connect Qt and libvlc libraries.
It contains core classes for main media playback and also some GUI
classes for faster media player development.
This package contains the %{name}-qml library.

%files  -n %{libnameqml}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/lib%{oname}Qml.so.%{major}
%{_libdir}/lib%{oname}Qml.so.%{major}.*
%{_libdir}/qt5/qml/%{oname}/lib%{oname}.so.%{major}*
%{_libdir}/qt5/qml/%{oname}/qmldir

#----------------------------------------------------------------------------

%package -n	%{develnameqml}
Summary:	Headers and development libraries for vlc-qt library (qml)
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Requires:	%{libnameqml} = %{EVRD}
Requires:	%{develname} = %{EVRD}
Provides:	%{name}-qml-devel = %{EVRD}

%description -n %{develnameqml}
Headers and development libraries for %{name}-qml library.

%files  -n %{develnameqml}
%doc CHANGELOG.md README.md LICENSE.md
%{_libdir}/cmake/%{oname}Qml/*.cmake
%{_libdir}/cmake/%{oname}/*.cmake
%{_libdir}/pkgconfig/lib%{oname}Qml.pc
%{_libdir}/lib%{oname}Qml.so
%{_libdir}/qt5/qml/%{oname}/lib%{oname}.so
%{_includedir}/%{oname}Qml/Qml.h
%{_includedir}/%{oname}Qml/QmlPlayer.h
%{_includedir}/%{oname}Qml/QmlSource.h
%{_includedir}/%{oname}Qml/QmlVideoObject.h
%{_includedir}/%{oname}Qml/QmlVideoOutput.h
%{_includedir}/%{oname}Qml/QmlVideoPlayer.h
%{_includedir}/%{oname}Qml/SharedExportQml.h

#----------------------------------------------------------------------------

%prep
%setup -q


%build
%cmake -DSYSTEM_QML=On
%make


%install
%make_install -C build


