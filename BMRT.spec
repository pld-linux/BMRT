Summary:	BMRT - Blue Moon rendering Tool
Summary(pl):	BMRT - 
Name:		BMRT
Version:	2.5
Release:	1
Copyright:	Other
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	%{name}%{version}h.linux-glibc2.tar.gz
URL:		http://www.bmrt.org/
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q -n %{name}%{version}

%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_includedir},%{_libdir},%{_datadir}/%{name}/shaders}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install lib/* $RPM_BUILD_ROOT%{_libdir}
install include/* $RPM_BUILD_ROOT%{_includedir}
install shaders/*.sl $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders
install shaders/*.slc $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders
install shaders/*.h $RPM_BUILD_ROOT%{_datadir}/%{name}/shaders

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/html/* License doc/*.pdf
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_includedir}/*.h
%attr(644,root,root) %{_datadir}/%{name}/shaders/[^*.linux.slc]
%attr(755,root,root) %{_datadir}/%{name}/shaders/*.linux.*
%attr(644,root,root) %{_libdir}/*.a
%attr(755,root,root) %{_libdir}/*.so
