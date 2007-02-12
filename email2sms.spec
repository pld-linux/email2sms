%include	/usr/lib/rpm/macros.perl
Summary:	An Email-to-SMS formatter
Summary(pl.UTF-8):   Formatowanie wiadomości Poczta->SMS
Name:		email2sms
Version:	0.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://adamspiers.org/computing/%{name}/email2sms.tar.gz
# Source0-md5:	c822bdc3a3af7fd44529189bf1e3ac26
URL:		http://adamspiers.org/computing/email2sms/
BuildRequires:	perl-base
BuildRequires:	perl-Lingua-EN-Squeeze
Requires:	perl-MIME-tools
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

%description -l pl.UTF-8
email2sms to napisany w Perlu filtr konwertujący listy elektroniczne
do postaci nadającej się do wysyłania jako wiadomość SMS. Główną
zaletą nad innymi programami tego typu jest to, że używa modułu CPAN
Lingua::EN::Squeeze, aby skompresować tekst do około 40% oryginalnego
rozmiaru, co pozwala zmieścić więcej w ograniczeniu do 160 znaków.
Program jest w pełni kompatybilny z MIME i ma wiele opcji, włącznie z
usuwaniem cytowanego tekstu. Idealny do używania z procmailem.
Załączony jest skrypt perlowy do wysyłania wyjścia przez typową
bramkę e-mail-SMS.

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
