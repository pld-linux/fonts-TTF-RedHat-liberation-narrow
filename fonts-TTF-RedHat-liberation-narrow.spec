Summary:	Fonts to replace commonly used Microsoft Windows Arial narrow fonts
Summary(pl.UTF-8):	Fonty zastępujące popularny zestaw Arial narrow z Microsoft Windows
Name:		fonts-TTF-RedHat-liberation-narrow
Version:	1.07.6
Release:	1
License:	GPL v2 + exceptions
Group:		Fonts
#Source0Download: https://github.com/liberationfonts/liberation-sans-narrow/releases
Source0:	https://github.com/liberationfonts/liberation-sans-narrow/files/2579430/liberation-narrow-fonts-%{version}.tar.gz
# Source0-md5:	9a968114b222d6a03430a750504a7b15
Source1:	liberation-fonts-narrow.conf
URL:		https://github.com/liberationfonts/liberation-sans-narrow
BuildRequires:	fontforge >= 20090923
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Obsoletes:	liberation-fonts-ttf
Conflicts:	fonts-TTF-RedHat-liberation < 2
Conflicts:	fonts-TTF-RedHat-liberation1 < 1.07.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
The Liberation Fonts are intended to be replacements for the three
most commonly used fonts on Microsoft systems.

This package includes Sans Narrow (a substitute for Arial narrow).

%description -l pl.UTF-8
Fonty Liberation mają być zamiennikami trzech najczęściej używanych
fontów z systemów Microsoftu.

Ten pakiet zawiera Sans Narrow (zamiennik dla Arial narrow).

%prep
%setup -q -n liberation-narrow-fonts-%{version}

%build
%{__make}

%{__mv} liberation-narrow-fonts-ttf-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_ttffontsdir},%{_sysconfdir}/fonts/conf.d,%{_datadir}/fontconfig/conf.avail}

cp -p *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/fontconfig/conf.avail/59-liberation-narrow.conf

ln -s %{_datadir}/fontconfig/conf.avail/59-liberation-narrow.conf $RPM_BUILD_ROOT%{_sysconfdir}/fonts/conf.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog License.txt README.rst TODO
%{_ttffontsdir}/LiberationSansNarrow-*.ttf
%{_datadir}/fontconfig/conf.avail/59-liberation-narrow.conf
%{_sysconfdir}/fonts/conf.d/59-liberation-narrow.conf
