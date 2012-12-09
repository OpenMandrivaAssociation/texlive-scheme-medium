# revision 18615
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-medium
Version:	20120307
Release:	1
Summary:	medium scheme (plain, latex, recommended packages, some languages)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-medium.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-binextra
Requires:	texlive-collection-context
Requires:	texlive-collection-documentation-english
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-langczechslovak
Requires:	texlive-collection-langdutch
Requires:	texlive-collection-langfrench
Requires:	texlive-collection-langgerman
Requires:	texlive-collection-langitalian
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-langportuguese
Requires:	texlive-collection-langspanish
Requires:	texlive-collection-langenglish
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-mathextra
Requires:	texlive-collection-metapost
Requires:	texlive-collection-texinfo
Requires:	texlive-collection-xetex
Requires:	texlive-collection-luatex
Requires:	texlive-collection-genericrecommended

%description
This is the medium TeX Live collection: it contains plain TeX,
LaTeX, many recommended packages, and support for some widely-
used European languages.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Wed Mar 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120307-1
+ Revision: 783144
- Import texlive-scheme-medium
- Import texlive-scheme-medium

