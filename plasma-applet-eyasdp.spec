%define	shortname	eyasdp
%define	longname	plasma_applet_%{shortname}

Name:		plasma-applet-%{shortname}
Version:	0.9.0
Release:	%mkrel 69.2
Summary:	System buttons plasmoid
License:	GPLv2
Group:		Graphical desktop/KDE
Url:		http://kde-look.org/content/show.php/eYaSDP?content=146530
Source0:	http://kde-look.org/CONTENT/content-files/146530-%{shortname}-%{version}.tar.bz2
Patch0:		eyasdp-0.9.0-ru.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
# configure also test for the packages below
BuildRequires:	phonon-devel
BuildRequires:	openssl-devel
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

%prep
%setup -q -n %{shortname}-%{version}
%patch0 -p1 -b .ru

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%find_lang %{longname}

%files -f %{longname}.lang
%{_kde_libdir}/kde4/plasma_applet_%{shortname}.so
%{_kde_services}/plasma-applet-%{shortname}.desktop




%changelog
* Thu Jan 05 2012 Andrey Bondrov <abondrov@mandriva.org> 0.9.0-69.2mdv2011.0
+ Revision: 757848
- imported package plasma-applet-eyasdp


* Thu Jan 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.9.0-69.2-mib2011.0
- Add patch with russian translation
- Add kdebase4-workspace-devel to BuildRequires

* Mon Dec 12 2011 Giovanni Mariani <mc2374@mclink.it> 0.9.0-69.1-mib2011.0
- New release 0.9.0
- Removed useless things with rpm5
- Added use of %%find_lang macro

* Mon Dec 06 2011 Giovanni Mariani <mc2374@mclink.it> 0.5.0-69.1-mib2011.0
- Rebuilded for Mdv 2011.0

* Fri Dec 02 2011 Giovanni Mariani <mc2374@mclink.it> 0.5.0-69.1mib2010.2
- Adapted to Mdv 2010.2 by the MIB (from a Mageia greek community package)
- Added BuildRoot, a couple of BReqs (see configure output) and a %%changelog
- Added a little patch to keep desktop-file-validate happy
- Made sure to use consistently the curly brackets for macro names
