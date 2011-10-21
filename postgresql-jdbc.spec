%define	pg_ver	9.1
Summary:	PostgreSQL JDBC driver
Summary(pl.UTF-8):	Sterownik JDBC do PostgreSQL-a
Name:		postgresql-jdbc
Version:	901
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://jdbc.postgresql.org/download/%{name}-%{pg_ver}-%{version}.src.tar.gz
# Source0-md5:	eab20a5cd5344a21f33a1768dd3f4f96
URL:		http://jdbc.postgresql.org/
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	ant >= 1.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PostgreSQL JDBC driver allows Java programs to connect to a PostgreSQL
database using standard, database independent Java code. It is a pure
Java (Type IV) implementation. The driver provides are reasonably
complete implementation of the JDBC 3 specification in addition to
some PostgreSQL specific extensions. Our goal is nothing short of full
compliance, but it's not there yet. Some features require additional
backend support and others just need someone to implement them.

%description -l pl.UTF-8
Sterownik JDBC do PostgreSQL-a pozwala programom w Javie łączyć się z
bazą danych PostgreSQL przy użyciu stanadrdowego, niezależnego od bazy
danych, kodu w Javie. Jest to implementacja w czystej Javie (Type IV).
Sterownik dostarcza prawie pełną implementację specyfikacji JDBC 3 z
dodatkiem rozszerzeń specyficznych dla PostgreSQL-a. Celem jest
osiągnięcie pełnej zgodności, ale do niej jeszcze trochę brakuje.
Niektóre możliwości wymagają dodatkowego wsparcia backendu, a inne po
prostu kogoś, kto je zaimplementuje.

%prep
%setup -q -n %{name}-%{pg_ver}-%{version}.src

%build
ant

cd doc
db2html pgjdbc.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

install jars/postgresql.jar $RPM_BUILD_ROOT%{_javadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README doc/pgjdbc
%{_javadir}/postgresql.jar
