# revision 29349
# category Package
# catalog-ctan /macros/latex/contrib/texpower
# catalog-date 2012-02-24 11:11:42 +0100
# catalog-license gpl
# catalog-version 0.2
Name:		texlive-texpower
Version:	0.2
Release:	8
Summary:	Create dynamic online presentations with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/texpower
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texpower.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-tpslifonts

%description
TeXPower is a bundle of packages intended to provide an all-
inclusive environment for designing pdf screen presentations to
be viewed in full-screen mode, especially for projecting
`online' with a video beamer. For some of its core functions,
it uses code derived from ppower4 packages. It is, however, not
a complete environment in itself: it relies on an existing
class for preparing slides (such as foiltex or seminar) or
another package such as pdfslide.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/texpower/automata.sty
%{_texmfdistdir}/tex/latex/texpower/fixseminar.sty
%{_texmfdistdir}/tex/latex/texpower/powersem.cls
%{_texmfdistdir}/tex/latex/texpower/texpower.sty
%{_texmfdistdir}/tex/latex/texpower/tpcolors.cfg
%{_texmfdistdir}/tex/latex/texpower/tplists.sty
%{_texmfdistdir}/tex/latex/texpower/tpoptions.cfg
%{_texmfdistdir}/tex/latex/texpower/tppstcol.sty
%{_texmfdistdir}/tex/latex/texpower/tpsem-a4.sty
%{_texmfdistdir}/tex/latex/texpower/tpsettings.cfg
%doc %{_texmfdistdir}/doc/latex/texpower/00readme.txt
%doc %{_texmfdistdir}/doc/latex/texpower/01install.txt
%doc %{_texmfdistdir}/doc/latex/texpower/02changes.txt
%doc %{_texmfdistdir}/doc/latex/texpower/FAQ-display.tex
%doc %{_texmfdistdir}/doc/latex/texpower/FAQ-printout.tex
%doc %{_texmfdistdir}/doc/latex/texpower/MakeExamples.sh
%doc %{_texmfdistdir}/doc/latex/texpower/__TPcfg.tex
%doc %{_texmfdistdir}/doc/latex/texpower/__TPindexing.tex
%doc %{_texmfdistdir}/doc/latex/texpower/__TPpreamble.tex
%doc %{_texmfdistdir}/doc/latex/texpower/bckwrdexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/bgndexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/contrib/00readme.txt
%doc %{_texmfdistdir}/doc/latex/texpower/contrib/config.landscapeplus
%doc %{_texmfdistdir}/doc/latex/texpower/contrib/tpmultiinc.tar
%doc %{_texmfdistdir}/doc/latex/texpower/divexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/dummy.java
%doc %{_texmfdistdir}/doc/latex/texpower/fancyexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/fig-1.mps
%doc %{_texmfdistdir}/doc/latex/texpower/fig-2.mps
%doc %{_texmfdistdir}/doc/latex/texpower/fig-3.mps
%doc %{_texmfdistdir}/doc/latex/texpower/foilsdemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/fulldemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/hilitexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/ifmslidemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/manual.pdf
%doc %{_texmfdistdir}/doc/latex/texpower/manual.tex
%doc %{_texmfdistdir}/doc/latex/texpower/mathexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/panelexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/parexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/pdfscrdemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/pdfslidemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/picexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/picltxexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/picpsexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/pp4sldemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/prosperdemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/seminardemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/simpledemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/slidesdemo.tex
%doc %{_texmfdistdir}/doc/latex/texpower/spanelexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/tabexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts.zip
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/00readme.txt
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/01install.txt
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/Makefile
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/slifontsexample.tex
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/tpslifonts.dtx
%doc %{_texmfdistdir}/doc/latex/texpower/tpslifonts/tpslifonts.ins
%doc %{_texmfdistdir}/doc/latex/texpower/verbexample.tex
#- source
%doc %{_texmfdistdir}/source/latex/texpower/Makefile
%doc %{_texmfdistdir}/source/latex/texpower/powersem.dtx
%doc %{_texmfdistdir}/source/latex/texpower/texpower-addons.dtx
%doc %{_texmfdistdir}/source/latex/texpower/texpower-cfg.dtx
%doc %{_texmfdistdir}/source/latex/texpower/texpower-doc.dtx
%doc %{_texmfdistdir}/source/latex/texpower/texpower.dtx
%doc %{_texmfdistdir}/source/latex/texpower/tpbundle.ins
%doc %{_texmfdistdir}/source/latex/texpower/tplists.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
