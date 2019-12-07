Name:		WizNote
Version:	2.8.2
Release:	1%{?dist}
Summary:	WizNote QT Client

Group:		Application
License:	GPLv3
URL:		http://wiz.cn/
Source0:	https://github.com/WizTeam/WizQTClient/archive/2.8.2.tar.gz#/WizQTClient-%{version}.tar.gz

BuildRequires:	cmake gcc
Requires:	qt5-qtbase qt5-qtwebengine qt5-qtwebsockets openssl qt5-qttools libstdc++

%description

 Cross platform cloud based note-taking application
 WizNote is a cross platform cloud based note-taking application.
 .
 support following platforms:
 1. windows xp/vista/7/8.
 2. Mac OSX.
 3. Linux
 3. Android/IOs.
 4. Web
 .
 please refer to WizNote home for more detailed info: http://www.wiznote.com.

%prep
%setup -qc


%build
cmake -DWIZNOTE_USE_QT5=YES -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release WizQTClient
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
/usr/local/
%doc



%changelog

