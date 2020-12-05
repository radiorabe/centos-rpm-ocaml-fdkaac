# CentOS RPM Specfile for ocaml-fdkaac

This repository contains the specfile for ocaml-fdkaac which is part of the [RaBe liquidsoap distribution](https://build.opensuse.org/project/show/home:radiorabe:liquidsoap).

Due to licencing reasons we cannot provide a binary package of ocaml-fdk-aac. Please build your own packages using the instauctions below.

## Usage

```bash
# install RPMfusion onfree because it contains fdk-aac-devel
dnf install -y \
  http://download1.rpmfusion.org/free/el/updates/8/x86_64/r/rpmfusion-free-release-8-0.1.noarch.rpm \
  http://download1.rpmfusion.org/nonfree/el/updates/8/x86_64/r/rpmfusion-nonfree-release-8-0.1.noarch.rpm

# the RaBe-LSD liquidsoap binaries are using an OCaml build chain based on a backport of fc33 ocaml
curl -o /etc/yum.repos.d/ocaml.repo \
  "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"

rpmdev-setuptree

spectool -R -g ocaml-fdkaac.spec

dnf builddep -y ocaml-fdkaac.spec

rpmbuild -ba ocaml-fdkaac.spec
```
