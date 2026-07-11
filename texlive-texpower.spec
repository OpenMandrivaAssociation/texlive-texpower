%global tl_name texpower
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Create dynamic online presentations with LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texpower
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(tpslifonts)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeXPower is a bundle of packages intended to provide an all-inclusive
environment for designing pdf screen presentations to be viewed in full-
screen mode, especially for projecting `online' with a video beamer. For
some of its core functions, it uses code derived from ppower4 packages.
It is, however, not a complete environment in itself: it relies on an
existing class for preparing slides (such as foiltex or seminar) or
another package such as pdfslide.

