Summary:	BMRT - Blue Moon Rendering Tools
Summary(pl.UTF-8):	Blue Moon Rendering Tools - Narzędzia do renderingu
Name:		BMRT
Version:	2.5
Release:	2
License:	Free use, no source
Group:		Applications/Graphics
Source0:	%{name}%{version}h.linux-glibc2.tar.gz
# Source0-md5:	dfbe508d03b352a01949679809cd3e06
URL:		http://www.bmrt.org/
ExclusiveArch:	%{ix86}
Requires:	compat-libstdc++-2.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BMRT is a ray tracer that has been used in the production of several
feature films, including A Bug's Life, Stuart Little, The Cell, Hollow
Man, and Woman on Top.

BMRT supports such features as ray traced reflections and shadows;
area lights; texture, environment, and shadow mapping; and fully
programmable surface, displacement, light, and volume shaders. BMRT's
input scene files and shaders are largely compatible with our
commercial renderer, Entropy, as well as those of PhotoRealistic
RenderMan.

No longer available. Use Aqsis (http://aqsis.sf.net/) instead.

%description -l pl.UTF-8
BMRT jest ray tracerem, który został użyty przy produkcji niektórych
filmów, takich jak A Bug's Life, Stuart Little, The Cell, Hollow Man,
Woman on Top.

BMRT obsługuje rzeczy takie jak odbicia i cienie; światła punktowe;
tekstury, środowisko, mapowanie cieni; w pełni programowalne
powierzchnie, zaburzenia, światła, cienie. Pliki wejściowe ze scenami
i cieniami BMRT są w dużej części zgodne z komercyjnym rendererem tej
samej firmy o nazwie Entropy, a także z programem PhotoRealistic
RenderMan.

BMRT nie jest już dostępny. Zamiast niego można używać Aqsis
(http://aqsis.sf.net/).

%prep
%setup -q -n %{name}%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_includedir},%{_libdir},%{_datadir}/%{name}/shaders}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install lib/* $RPM_BUILD_ROOT%{_libdir}
install include/* $RPM_BUILD_ROOT%{_includedir}
install shaders/*.sl $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders
install shaders/*.slc $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders
install shaders/*.h $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/html/* License doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shaders
%{_datadir}/%{name}/shaders/*.sl
%{_datadir}/%{name}/shaders/*[!x].slc
%attr(755,root,root) %{_datadir}/%{name}/shaders/*.linux.slc
%{_libdir}/*.a
%{_includedir}/*.h
