Summary:	BMRT - Blue Moon Rendering Tools
Summary(pl):	Blue Moon Rendering Tools - Narzêdzia do renderingu
Name:		BMRT
Version:	2.5
Release:	2
License:	Free use, no source
Group:		Applications/Graphics
Source0:	%{name}%{version}h.linux-glibc2.tar.gz
URL:		http://www.bmrt.org/
ExclusiveArch:	%{ix86}
Requires:	libstdc++-compat
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

No longer available. Use Aqsis (http://aqsis.sf.net) instead.

%description -l pl
BMRT jest ray tracerem, który zosta³ u¿yty przy produkcji niektórych
filmów, takich jak A Bug's Life, Stuart Little, The Cell, Hollow Man,
Woman on Top.

BMRT obs³uguje rzeczy takie jak odbicia i cienie; ¶wiat³a punktowe;
tekstury, ¶rodowisko, mapowanie cieni; w pe³ni programowalne
powierzchnie, zaburzenia, ¶wiat³a, cienie. Pliki wej¶ciowe ze scenami
i cieniami BMRT s± w du¿ej czê¶ci zgodne z komercyjnym rendererem tej
samej firmy o nazwie Entropy, a tak¿e z programem PhotoRealistic
RenderMan.

BMRT nie jest ju¿ dostêpny. Zamiast niego mo¿na u¿ywaæ Aqsis
(http://aqsis.sf.net).

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
install -m 755 shaders/*.linux.slc $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders
install shaders/*.h $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/html/* License doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*.h
%attr(-,root,root) %{_datadir}/%{name}/shaders/*
%{_libdir}/*.a
%attr(755,root,root) %{_libdir}/*.so
