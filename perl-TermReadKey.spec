Name:           perl-TermReadKey
Version:        2.38
Release:        2
Summary:        A perl module for simple terminal control
License:        (Copyright only) and (Artistic or GPL+)
URL:            https://metacpan.org/release/TermReadKey
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
# Build
BuildRequires:  coreutils, findutils, gcc, make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
Requires:       perl(:MODULE_COMPAT_%(perl -V:version | cut -d"'" -f 2))

%{?perl_default_filter}

%description
This module, ReadKey, provides ioctl control for terminals and Win32
consoles so the input modes can be changed (thus allowing reads of a single
character at a time), and also provides non-blocking reads of stdin, as well
as several other terminal related features, including retrieval/modification
of the screen size, and retrieval/modification of the control characters.

%prep
%setup -q -n TermReadKey-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build OPTIMIZE="%{optflags}"

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name '*.bs' -a -size 0 -delete

%check
make test

%files
%defattr(-,root,root)
%doc README
%{perl_vendorarch}/*
%{perl_vendorarch}/auto/*

%package_help
%files help
%defattr(-,root,root)
%doc Changes example
%{_mandir}/man3/*

%changelog
* Mon Sep 23 2019 shenyangyang<shenyangyang4@huawei.com> - 2.38-2
- Type:enhancement
- ID:NA
- SUG:NA
- DESC:revise requires of perl

* Fri Aug 30 2019 hexiaowen <hexiaowen@huawei.com> 2.38-1
- Package init
