%include	/usr/lib/rpm/macros.perl
Summary:	An Email-to-SMS formatter
Summary(pl):	Formatowanie wiadomo¶ci Poczta->SMS
Name:		email2sms
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://adamspiers.org/computing/%{name}/email2sms.tar.gz
URL:		http://adamspiers.org/computing/email2sms/
BuildRequires:	perl
BuildRequires:	perl-Lingua-EN-Squeeze
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
email2sms is a filter written in Perl which converts an e-mail into a
form suitable for sending as an SMS message. Its main advantage over
the alternatives is that it uses the CPAN module Lingua::EN::Squeeze
to compress the text down to as little as 40% of its original size, so
you can get much more of your e-mail into the 160 character limit
imposed by SMS. It is fully MIME compatible, and has many configurable
options, including removal of quoted text. Ideal for use with
procmail. A Perl script for sending the output to a typical e-mail to
SMS web gateway is included.

%description -l pl
email2sms to napisany w Perlu filtr konwertuj±cy listy elektroniczne
do postaci nadaj±cej siê do wysy³ania jako wiadomo¶æ SMS. G³ówn±
zalet± nad innymi programami tego typu jest to, ¿e u¿ywa modu³u CPAN
Lingua::EN::Squeeze, aby skompresowaæ tekst do oko³o 40% oryginalnego
rozmiaru, co pozwala zmie¶ciæ wiêcej w ograniczeniu do 160 znaków.
Program jest w pe³ni kompatybilny z MIME i ma wiele opcji, w³±cznie z
usuwaniem cytowanego tekstu. Idealny do u¿ywania z procmailem.
Za³±czony jest skrypt perlowy do wysy³ania wyj¶cia przez typow±
bramkê e-mail-SMS.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install email2sms $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog *.html sample*
%attr(755,root,root) %{_bindir}/*
