%define base_name drakx-installer-stage2
%define name %{base_name}-tmb
%define version 12.16
%define release %mkrel 1

Summary: DrakX installer stage2 image modified for kernel-tmb
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{base_name}-%{version}.tar.lzma
License: GPLv2+
Group: Development/Other
Url: http://wiki.mandriva.com/Tools/DrakX
BuildRoot: %{_tmppath}/%{base_name}-%{version}-%{release}-buildroot

BuildRequires: squashfs-tools >= 4.0
BuildRequires: libx11-devel perl-devel libldetect-devel drakx-installer-binaries parted-devel
BuildRequires: perl-Gtk2 perl-Glib perl-XML-Parser perl-Curses perl-Curses-UI perl-Term-ReadKey
BuildRequires: perl-Locale-gettext packdrake
BuildRequires: drakx-net >= 0.43
BuildRequires: drakx-kbd-mouse-x11 >= 0.69
BuildRequires: rpm-mandriva-setup >= 1.48
BuildRequires: perl-MDK-Common >= 1.2.12
BuildRequires: urpmi >= 6.22.4
BuildRequires: perl-URPM >= 3.26
BuildRequires: meta-task
BuildRequires: ldetect-lst >= 0.1.222
BuildRequires: draksnapshot
# progs
BuildRequires: drakx-installer-matchbox
BuildRequires: e2fsprogs >= 1.41.3-3mnb
BuildRequires: dosfstools 
BuildRequires: task-x11 libx11-devel libxxf86misc-devel x11-driver-video-fbdev
BuildRequires: setserial pciutils mt-st reiserfsprogs jfsutils reiser4progs
BuildRequires: xfsprogs pcmcia-cs gettext ash linuxwacom
BuildRequires: fonts-ttf-bengali fonts-ttf-bitstream-vera fonts-ttf-lohit fonts-ttf-thai fonts-ttf-devanagari
BuildRequires: fb2png ntfsprogs ia_ora-gnome brltty
BuildRequires: lvm2 glibc-i18ndata
BuildRequires: dmraid mdadm quota
BuildRequires: losetup xmodmap xset monitor-edid locales
BuildRequires: perl-Gtk2-WebKit mandriva-doc-installer-help
BuildRequires: nfs-utils-clients

%description
This is the stage2 image for Mandriva DrakX installer modified for kernel-tmb.

%prep
%setup -q -n %{base_name}-%{version}

%build
make -C tools
make -C perl-install/install
rpm -qa | sort > build-rpms.lst

%install
rm -rf $RPM_BUILD_ROOT

dest=$RPM_BUILD_ROOT%{_libdir}/%name
mkdir -p $dest
make -C perl-install/install install ROOTDEST=$dest
make -C tools install ROOTDEST=$dest

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc build-rpms.lst
%{_libdir}/%name

