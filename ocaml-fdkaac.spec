Name:     ocaml-fdkaac

Version:  0.3.2
Release:  0.1%{?dist}
Summary:  OCaml bindings for fdkaac
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-fdkaac
Source0:  https://github.com/savonet/ocaml-fdkaac/archive/%{version}.tar.gz?#/%{name}-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-dune-devel
BuildRequires: fdk-aac-devel
Requires:      fdk-aac
Provides:      ocaml(Fdkaac_dynlink)

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
dune build

%install
dune install \
  --prefix %{buildroot} \
  --libdir %{buildroot}$(ocamlfind printconf destdir)
rm -rf %{buildroot}/doc


%files
%doc README.md CHANGES
%license COPYING
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
