Name:     ocaml-fdkaac

Version:  0.2.1
Release:  1
Summary:  OCaml bindings for fdkaac
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-fdkaac
Source0:  https://github.com/savonet/ocaml-fdkaac/releases/download/%{version}/ocaml-fdkaac-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: fdk-aac-devel
Requires:      fdk-aac

%description
OCAML bindings for fdkaac

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       fdk-aac-devel


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/stublibs
make install

%files
%doc CHANGES COPYING README
%{_libdir}/ocaml/*
%exclude %{_libdir}/ocaml/*/*.a
%exclude %{_libdir}/ocaml/*/*.cmxa
%exclude %{_libdir}/ocaml/*/*.mli

%files devel
%defattr(-,root,root,-)
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.cmxs
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META
