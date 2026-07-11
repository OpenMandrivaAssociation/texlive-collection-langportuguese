%global tl_name collection-langportuguese
%global tl_revision 73303

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Portuguese
Group:		Publishing
URL:		https://www.ctan.org/pkg/collection-langportuguese
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langportuguese.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(babel-portuges)
Requires:	texlive(beamer-tut-pt)
Requires:	texlive(collection-basic)
Requires:	texlive(cursolatex)
Requires:	texlive(feupphdteses)
Requires:	texlive(hyphen-portuguese)
Requires:	texlive(latex-via-exemplos)
Requires:	texlive(latexcheat-ptbr)
Requires:	texlive(lshort-portuguese)
Requires:	texlive(numberpt)
Requires:	texlive(ordinalpt)
Requires:	texlive(ptlatexcommands)
Requires:	texlive(tabularray-abnt)
Requires:	texlive(xypic-tut-pt)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Support for Portuguese and Brazilian Portuguese.

