Summary:	PostgreSQL JDBC driver
Summary(pl):	Sterownik JDBC do PostgreSQL-a
Name:		postgresql-jdbc
Version:	310
Release:	1
License:	BSD
Group:		Development/Languages/Java
Source0:	http://jdbc.postgresql.org/download/%{name}-8.0-%{version}.src.tar.gz
# Source0-md5:	036e05ac278109b56bed125ebfd9c159
URL:		http://jdbc.postgresql.org/
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	docbook-utils
BuildRequires:	jakarta-ant >= 1.5
BuildRoot:	%{tmpdir}/%{name}-%{postgresql_version}-root-%(id -u -n)

%description
PostgreSQL JDBC driver allows Java programs to connect to a PostgreSQL
database using standard, database independent Java code. It is a pure
Java (Type IV) implementation. The driver provides are reasonably
complete implementation of the JDBC 3 specification in addition to
some PostgreSQL specific extensions. Our goal is nothing short of full
compliance, but it's not there yet. Some features require additional
backend support and others just need someone to implement them.

%description -l pl
Sterownik JDBC do PostgreSQL-a pozwala programom w Javie ³±czyæ siê z
baz± danych PostgreSQL przy u¿yciu stanadrdowego, niezale¿nego od bazy
danych, kodu w Javie. Jest to implementacja w czystej Javie (Type IV).
Sterownik dostarcza prawie pe³n± implementacjê specyfikacji JDBC 3 z
dodatkiem rozszerzeñ specyficznych dla PostgreSQL-a. Celem jest
osi±gniêcie pe³nej zgodno¶ci, ale do niej jeszcze trochê brakuje.
Niektóre mo¿liwo¶ci wymagaj± dodatkowego wsparcia backendu, a inne po
prostu kogo¶, kto je zaimplementuje.

%prep
%setup -q -n %{name}-8.0-%{version}.src

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
