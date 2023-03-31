Name:		texlive-collection-langportuguese
Epoch:		1
Version:	54074
Release:	2
Summary:	Portuguese
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langportuguese.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-babel-portuges
Requires:	texlive-beamer-tut-pt
Requires:	texlive-cursolatex
Requires:	texlive-feupphdteses
Requires:	texlive-hyphen-portuguese
Requires:	texlive-latexcheat-ptbr
Requires:	texlive-lshort-portuguese
Requires:	texlive-ordinalpt
Requires:	texlive-xypic-tut-pt

%description
Support for Portuguese.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
