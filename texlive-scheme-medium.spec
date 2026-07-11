%global tl_name scheme-medium
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	medium scheme (small + more packages and languages)
Group:		Publishing
URL:		https://www.ctan.org/pkg/scheme-medium
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/scheme-medium.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(collection-basic)
Requires:	texlive(collection-binextra)
Requires:	texlive(collection-context)
Requires:	texlive(collection-fontsrecommended)
Requires:	texlive(collection-fontutils)
Requires:	texlive(collection-langczechslovak)
Requires:	texlive(collection-langenglish)
Requires:	texlive(collection-langeuropean)
Requires:	texlive(collection-langfrench)
Requires:	texlive(collection-langgerman)
Requires:	texlive(collection-langitalian)
Requires:	texlive(collection-langpolish)
Requires:	texlive(collection-langportuguese)
Requires:	texlive(collection-langspanish)
Requires:	texlive(collection-latex)
Requires:	texlive(collection-latexrecommended)
Requires:	texlive(collection-luatex)
Requires:	texlive(collection-mathscience)
Requires:	texlive(collection-metapost)
Requires:	texlive(collection-plaingeneric)
Requires:	texlive(collection-texworks)
Requires:	texlive(collection-xetex)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is the medium TeX Live collection: it contains plain TeX, LaTeX,
many recommended packages, and support for most European languages.

