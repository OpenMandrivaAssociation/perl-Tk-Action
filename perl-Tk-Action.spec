%define upstream_name    Tk-Action
%define upstream_version 1.093390

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Action abstraction for tk
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Has::Sugar)
BuildRequires: perl(MooseX::SemiAffordanceAccessor)
BuildRequires: perl(Test::More)
BuildRequires: perl(Tk::Sugar)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Menu entries are often also available in toolbars or other widgets. And
sometimes, we want to enable or disable a given action, and this means
having to update everywhere this action is allowed.

This module helps managing actions in a the Tk manpage GUI: just create a
new object, associate some widgets and bindings with 'add_widget()' and
then de/activate the whole action at once with 'enable()' or 'disable()'.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*


