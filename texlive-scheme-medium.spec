# revision 30457
# category Scheme
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-scheme-medium
Version:	20170504
Release:	1
Summary:	medium scheme (small + more packages and languages)
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
Requires:	texlive-collection-fontsrecommended
Requires:	texlive-collection-fontutils
Requires:	texlive-collection-genericrecommended
Requires:	texlive-collection-langczechslovak
Requires:	texlive-collection-langenglish
Requires:	texlive-collection-langeuropean
Requires:	texlive-collection-langfrench
Requires:	texlive-collection-langgerman
Requires:	texlive-collection-langitalian
Requires:	texlive-collection-langpolish
Requires:	texlive-collection-langportuguese
Requires:	texlive-collection-langspanish
Requires:	texlive-collection-latex
Requires:	texlive-collection-latexrecommended
Requires:	texlive-collection-luatex
Requires:	texlive-collection-mathextra
Requires:	texlive-collection-metapost
Requires:	texlive-collection-plainextra
Requires:	texlive-collection-xetex

%description
This is the medium TeX Live collection: it contains plain TeX,
LaTeX, many recommended packages, and support for most European
languages.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
