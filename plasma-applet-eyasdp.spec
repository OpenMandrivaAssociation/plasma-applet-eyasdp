%define	shortname	eyasdp
%define	longname	plasma_applet_%{shortname}

Summary:	System buttons plasmoid
Name:		plasma-applet-%{shortname}
Version:	1.2.0
Release:	4
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php/eYaSDP?content=146530
Source0:	http://kde-look.org/CONTENT/content-files/146530-%{shortname}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(phonon)
Requires:	kdebase4-runtime

%description
eYaSDP is a plasmoid that allows to set a number of system buttons in your
panel or desktop for comfortable and quick access.
Features:
  - Actions: Shut-down, Reboot, Log-out, Lock screen, Hibernate, Suspend,
    Switch user and Turn-off screen.
  - Customizable number of buttons.
  - Contextual menu actions.
  - Customizable icons.
  - It scales to fit your panel size.

%files -f %{longname}.lang
%{_kde_libdir}/kde4/plasma_applet_%{shortname}.so
%{_kde_services}/plasma-applet-%{shortname}.desktop

#----------------------------------------------------------------------------

%prep
%setup -q -n %{shortname}-%{version}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{longname}

