%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from jquery-rails-2.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name jquery-rails

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 4.0.4
Release: 4%{?dist}
Summary: Use jQuery with Rails 4+
Group: Development/Languages
License: MIT
URL: http://rubygems.org/gems/jquery-rails
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:      %{?scl_prefix_ruby}ruby(release)
Requires:      %{?scl_prefix_ruby}ruby(rubygems) >= 1.3.6
Requires:      %{?scl_prefix}rubygem(railties) >= 4.2.0
Requires:      %{?scl_prefix}rubygem(thor) >= 0.14
Requires:      %{?scl_prefix}rubygem(thor) < 2.0
Requires:      %{?scl_prefix}rubygem(rails-dom-testing) => 1.0
Requires:      %{?scl_prefix}rubygem(rails-dom-testing) < 2
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildArch:     noarch
Provides:      %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This gem provides jQuery and the jQuery-ujs driver for your Rails 4+
application.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

# Keep bundled jQuery
#rm .%%{gem_instdir}/vendor/assets/javascripts/jquery{,2}.*

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# no tests :( but they are comming back again shortly!
# see https://github.com/rails/jquery-rails/pull/56
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
# bunch of bundled JS files here
%{gem_instdir}/vendor
%exclude %{gem_cache}
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/Gemfile.lock
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/CONTRIBUTING.md
%doc %{gem_instdir}/VERSIONS.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/jquery-rails.gemspec

%changelog
* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.0.4-4
- Fix Require of rubygem-railties

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 4.0.4-3
- Update to 4.0.4

* Mon Feb 02 2015 Vít Ondruch <vondruch@redhat.com> - 3.1.0-2
- Fix thor dependency.

* Mon May 26 2014 Josef Stribny <jstribny@redhat.com> - 3.1.0-1
- Update to jquery-rails 3.1.0
  - This resolves: rhbz#1086262

* Thu Feb 06 2014 Josef Stribny <jstribny@redhat.com> - 3.0.4-3
- Fix license to MIT

* Wed Oct 23 2013 Josef Stribny <jstribny@redhat.com> - 3.0.4-2
- Convert to scl

* Wed Oct 23 2013 Josef Stribny <jstribny@redhat.com> - 3.0.4-1
- Update to jquery-rails 3.0.4

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 14 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 2.0.2-1
- Initial package
