# Leave this alone, please.
%global target out/Release

# %%{nil} for Stable; -beta for Beta; -dev for Devel
# dash in -beta and -dev is intentional !
%global chromium_channel %{nil}
%global chromium_browser_channel chromium-browser%{chromium_channel}
%global chromium_path %{_libdir}/chromium-browser%{chromium_channel}
%global crd_path %{_libdir}/chrome-remote-desktop

# We don't want any libs in these directories to generate Provides
# Requires is trickier. 

%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global privlibs libaccessibility|libaura_extra|libaura|libbase_i18n|libbase|libblink_common|libblink_core|libblink_modules|libblink_platform|libblink_web|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture|libcc_blink|libcc_ipc|libcc_proto|libcc|libcc_surfaces|libchromium_sqlite3|libcloud_policy_proto_generated_compile|libcloud_policy_proto|libcommon|libcompositor|libcontent|libcrcrypto|libdbus|libdevice_battery|libdevice_core|libdevice_event_log|libdevice_gamepad|libdevice_geolocation|libdevices|libdevice_vibration|libdisplay_compositor|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libevents_base|libevents_devices_x11|libevents_ipc|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfont_service_library|libgcm|libgeometry|libgesture_detection|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_x11|libgin|libgles2_c_lib|libgles2_implementation|libgles2_utils|libGLESv2|libgl_init|libgl_wrapper|libgpu|libgtk2ui|libicui18n|libicuuc|libipc|libkeyboard|libkeyboard_with_content|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libmedia_blink|libmedia_gpu|libmedia|libmemory_coordinator_browser|libmemory_coordinator_child|libmemory_coordinator_common|libmessage_center|libmidi|libmojo_blink_lib|libmojo_common_lib|libmojo_ime_lib|libmojo_public_system|libmojo_system_impl|libnative_theme|libnet|libnet_with_v8|libonc|libplatform|libpolicy_component|libpolicy_proto|libpower_save_blocker|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|librange|libsandbox_services|libseccomp_bpf|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing|libtranslator|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_library|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_prefs|libv8|libviews|libwebdata_common|libweb_dialogs|libwebview|libwidevinecdm|libwm|libwtf|libx11_events_platform|libx11_window|libbindings|libgeolocation|libmojo_public_system_cpp|libtime_zone_monitor|libdevice_base|libcc_animation|libcpp|libdevice_base|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libgeneric_sensor|libgl_in_process_context|libjs|libpower_monitor|libv8_libbase|libsensors|libdevice_vr|libcc_paint|libgtk3ui
%global __requires_exclude ^(%{privlibs})\\.so

#%if 0
# Chromium's fork of ICU is now something we can't unbundle.
# This is left here to ease the change if that ever switches.
#BuildRequires:  libicu-devel >= 5.4
#%global bundleicu 0
#%else
#%global bundleicu 1
#%endif

%global bundlere2 1

# Chromium breaks on wayland, hidpi, and colors with gtk3 enabled.
%global gtk3 0

%if 0%{?rhel} == 7
%global bundleopus 1
%global bundleharfbuzz 1
%else
%global bundleharfbuzz 0
%global bundleopus 1
%endif

### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromoting_client_id 449907151817-8vnlfih032ni8c4jjps9int9t86k546t.apps.googleusercontent.com 

%global debug_package %{nil}
%global build_for_x86_64 1
%global build_for_i386 1
%define opera_chan opera-stable
%define opera_ver 44.0.2510.1159

Name:		%{opera_chan}-libffmpeg
Version:	57.0.2987.133
%if 0%{?fedora} >= 25
Release:	1%{?dist}.R
%else
Release:	1%{?dist}
%endif
Epoch:		5
Summary:	Additional FFmpeg library for Opera Web browser providing H264 and MP4 support
Group:		Applications/Internet
License:	BSD, LGPL
Url:		https://gist.github.com/lukaszzek/ec04d5c953226c062dac

Source0:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
Source1:	depot_tools.git-master.tar.gz

### Chromium Fedora Patches ###
# https://groups.google.com/a/chromium.org/forum/#!topic/gn-dev/7nlJv486bD4
Patch0:	chromium-53.0.2785.92-last-commit-position.patch
Patch1:	chromium-57.0.2987.98-gcc48-compat-version-stdatomic.patch

# We can assume gcc and binutils.
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	atk-devel
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
#BuildRequires:	desktop-file-utils
BuildRequires:	expat-devel
BuildRequires:	flex
BuildRequires:	fontconfig-devel
BuildRequires:	GConf2-devel
BuildRequires:	glib2-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gtk2-devel
BuildRequires:	glibc-devel
BuildRequires:	gperf
BuildRequires:	libatomic
BuildRequires:	libcap-devel
BuildRequires:	libdrm-devel
BuildRequires:	libgcrypt-devel
#BuildRequires:	libudev-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXtst-devel
BuildRequires:	nss-devel
#BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel

# for /usr/bin/appstream-util
# BuildRequires: libappstream-glib

# Fedora tries to use system libs whenever it can.
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	elfutils-libelf-devel
BuildRequires:	flac-devel
#BuildRequires:	hwdata
#BuildRequires:	kernel-headers
#BuildRequires:	libevent-devel
BuildRequires:	libffi-devel
#%if 0%{?bundleicu}
# If this is true, we're using the bundled icu.
# We'd like to use the system icu every time, but we cannot always do that.
#%else
# Not newer than 54 (at least not right now)
#BuildRequires:	libicu-devel
#= 54.1
#%endif
#BuildRequires:	libjpeg-devel
#BuildRequires:	libpng-devel
#BuildRequires:	libudev-devel
# We don't use libvpx anymore because Chromium loves to
# use bleeding edge revisions here that break other things
# ... so we just use the bundled libvpx.
# Same is true for libwebp.
#BuildRequires:	libxslt-devel
# Same here, it seems.
#BuildRequires:	libyuv-devel
%if %{bundleopus}
# Do nothing
%else
BuildRequires:	opus-devel
%endif
BuildRequires:	perl(Switch)
#%if 0%{gtk3}
BuildRequires:	pkgconfig(gtk+-3.0)
#%endif
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	python-beautifulsoup4
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-html5lib
%if 0%{?rhel} == 7
BuildRequires:	python-jinja2-28
%else
BuildRequires:	python-jinja2
%endif
BuildRequires:	python-markupsafe
BuildRequires:	python-ply
BuildRequires:	python-simplejson
%if 0%{?bundlere2}
# Using bundled bits, do nothing.
%else
Requires:	re2 >= 20160401
BuildRequires:	re2-devel >= 20160401
%endif
#BuildRequires:	speech-dispatcher-devel
BuildRequires:	yasm
BuildRequires:	pkgconfig(gnome-keyring-1)
# remote desktop needs this
#BuildRequires:	pam-devel
#BuildRequires:	systemd

Requires:	%{opera_chan} >= 5:%{opera_ver}

%if 0%{?build_for_x86_64}
%if !0%{?build_for_i386}
ExclusiveArch:    x86_64
%else
ExclusiveArch:    x86_64 i686
%endif
%else
%if 0%{?build_for_i386}
ExclusiveArch:    i686
%endif
%endif

%description
Due to changes in Chromium, Opera is no longer able to use the system FFmpeg
library for H264 video playback on Linux, so H264-encoded videos fail to play by
default (but HTML5 video encoded using different formats, like webm, work). For
legal reasons, Opera may not be distributed with H264 compatible FFmpeg library
included into package.

It's possible to build the extra version of Chromium modified FFmpeg providing
H264 and MP4 support. Opera-libffmpeg package includes this library.

%prep
%setup -q -T -c -n depot_tools -a 1
%setup -q -n chromium-%{version}

### Chromium Fedora Patches ###
%patch0 -p1 -b .lastcommit
%patch1 -p1 -b .gcc48-compat-version-stdatomic

export CC="gcc"
export CXX="g++"
export AR="ar"
export RANLIB="ranlib"

CHROMIUM_BROWSER_GN_DEFINES=""
CHROMIUM_BROWSER_GN_DEFINES+=' is_debug=false'
%ifarch x86_64
CHROMIUM_BROWSER_GN_DEFINES+=' system_libdir="lib64"'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' google_api_key="%{api_key}" google_default_client_id="%{default_client_id}" google_default_client_secret="%{default_client_secret}"'
CHROMIUM_BROWSER_GN_DEFINES+=' is_clang=false use_sysroot=false use_gio=true use_pulseaudio=true icu_use_data_file=true'
CHROMIUM_BROWSER_GN_DEFINES+=' ffmpeg_branding="ChromeOS" proprietary_codecs=true'
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=true is_component_build=true'
CHROMIUM_BROWSER_GN_DEFINES+=' use_gold=false'
CHROMIUM_BROWSER_GN_DEFINES+=' treat_warnings_as_errors=false'
export CHROMIUM_BROWSER_GN_DEFINES

# Remove most of the bundled libraries. Libraries specified below (taken from
# Gentoo's Chromium ebuild) are the libraries that needs to be preserved.
build/linux/unbundle/remove_bundled_libraries.py \
	'third_party/ffmpeg' \
	'third_party/adobe' \
	'third_party/flac' \
	'third_party/harfbuzz-ng' \
	'third_party/icu' \
	'third_party/inspector_protocol' \
	'v8/third_party/inspector_protocol' \
	'third_party/cld_3' \
	'base/third_party/libevent' \
	'third_party/libjpeg_turbo' \
	'third_party/libpng' \
	'third_party/libsrtp' \
	'third_party/libwebp' \
	'third_party/libxml' \
	'third_party/libxslt' \
	'third_party/openh264' \
	'third_party/re2' \
	'third_party/snappy' \
	'third_party/speech-dispatcher' \
	'third_party/usb_ids' \
	'third_party/xdg-utils' \
	'third_party/yasm' \
	'third_party/zlib' \
	'base/third_party/dmg_fp' \
	'base/third_party/dynamic_annotations' \
	'base/third_party/icu' \
	'base/third_party/nspr' \
	'base/third_party/superfasthash' \
	'base/third_party/symbolize' \
	'base/third_party/valgrind' \
	'base/third_party/xdg_mime' \
	'base/third_party/xdg_user_dirs' \
	'breakpad/src/third_party/curl' \
	'chrome/third_party/mozilla_security_manager' \
	'courgette/third_party' \
	'native_client_sdk/src/libraries/third_party/newlib-extras' \
	'native_client/src/third_party/dlmalloc' \
	'native_client/src/third_party/valgrind' \
	'net/third_party/mozilla_security_manager' \
	'net/third_party/nss' \
	'third_party/WebKit' \
	'third_party/analytics' \
	'third_party/angle' \
	'third_party/angle/src/common/third_party/numerics' \
	'third_party/angle/src/third_party/compiler' \
	'third_party/angle/src/third_party/libXNVCtrl' \
	'third_party/angle/src/third_party/murmurhash' \
	'third_party/angle/src/third_party/trace_event' \
	'third_party/blanketjs' \
	'third_party/boringssl' \
	'third_party/brotli' \
	'third_party/cacheinvalidation' \
	'third_party/catapult' \
	'third_party/catapult/tracing/third_party/d3' \
	'third_party/catapult/tracing/third_party/gl-matrix' \
	'third_party/catapult/tracing/third_party/jszip' \
	'third_party/catapult/tracing/third_party/mannwhitneyu' \
        'third_party/catapult/third_party/polymer' \
	'third_party/catapult/third_party/py_vulcanize' \
	'third_party/catapult/third_party/py_vulcanize/third_party/rcssmin' \
	'third_party/catapult/third_party/py_vulcanize/third_party/rjsmin' \
        'third_party/ced' \
	'third_party/cld_2' \
	'third_party/cros_system_api' \
	'third_party/devscripts' \
	'third_party/dom_distiller_js' \
	'third_party/expat' \
	'third_party/fips181' \
        'third_party/flatbuffers' \
	'third_party/flot' \
	'third_party/google_input_tools' \
	'third_party/google_input_tools/third_party/closure_library' \
	'third_party/google_input_tools/third_party/closure_library/third_party/closure' \
	'third_party/hunspell' \
	'third_party/iccjpeg' \
	'third_party/jinja2' \
	'third_party/jstemplate' \
	'third_party/khronos' \
	'third_party/leveldatabase' \
	'third_party/libXNVCtrl' \
	'third_party/libaddressinput' \
	'third_party/libjingle' \
	'third_party/libphonenumber' \
	'third_party/libsecret' \
	'third_party/libsrtp' \
	'third_party/libudev' \
	'third_party/libusb' \
	'third_party/libvpx' \
	'third_party/libvpx/source/libvpx/third_party/x86inc' \
	'third_party/libxml/chromium' \
	'third_party/libwebm' \
	'third_party/libyuv' \
	'third_party/lss' \
	'third_party/lzma_sdk' \
	'third_party/mesa' \
	'third_party/modp_b64' \
	'third_party/mt19937ar' \
	'third_party/openmax_dl' \
	'third_party/opus' \
	'third_party/ots' \
	'third_party/pdfium' \
	'third_party/pdfium/third_party/agg23' \
	'third_party/pdfium/third_party/base' \
	'third_party/pdfium/third_party/bigint' \
	'third_party/pdfium/third_party/freetype' \
	'third_party/pdfium/third_party/lcms2-2.6' \
	'third_party/pdfium/third_party/libjpeg' \
	'third_party/pdfium/third_party/libopenjpeg20' \
	'third_party/pdfium/third_party/libpng16' \
	'third_party/pdfium/third_party/libtiff' \
	'third_party/pdfium/third_party/zlib_v128' \
	'third_party/polymer' \
	'third_party/protobuf' \
	'third_party/protobuf/third_party/six' \
	'third_party/ply' \
	'third_party/qcms' \
	'third_party/qunit' \
	'third_party/sfntly' \
	'third_party/sinonjs' \
	'third_party/skia' \
	'third_party/smhasher' \
	'third_party/sqlite' \
	'third_party/tcmalloc' \
	'third_party/usrsctp' \
	'third_party/web-animations-js' \
	'third_party/webdriver' \
	'third_party/webrtc' \
	'third_party/widevine' \
	'third_party/woff2' \
	'third_party/x86inc' \
	'third_party/zlib/google' \
	'url/third_party/mozilla' \
	'v8/src/third_party/valgrind' \
	--do-remove

# Look, I don't know. This package is spit and chewing gum. Sorry.
rm -rf third_party/jinja2
ln -s %{python_sitelib}/jinja2 third_party/jinja2
rm -rf third_party/markupsafe
ln -s %{python_sitearch}/markupsafe third_party/markupsafe
# We should look on removing other python packages as well i.e. ply

export PATH=$PATH:%{_builddir}/depot_tools

build/linux/unbundle/replace_gn_files.py --system-libraries \
	flac \
%if 0%{?bundleharfbuzz}
%else
	harfbuzz-ng \
%endif
%if %{bundleopus}
%else
	opus \
%endif
%if 0%{?bundlere2}
%else
	re2 \
%endif
	yasm

tools/gn/bootstrap/bootstrap.py -v --gn-gen-args "$CHROMIUM_BROWSER_GN_DEFINES"
%{target}/gn gen --args="$CHROMIUM_BROWSER_GN_DEFINES" %{target}

# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h

%build

../depot_tools/ninja -C %{target} -vvv libffmpeg.so

%install
mkdir -p %{buildroot}%{_libdir}/%{opera_chan}/lib_extra
install -m 644 %{_builddir}/chromium-%{version}/out/Release/libffmpeg.so %{buildroot}%{_libdir}/%{opera_chan}/lib_extra/

%files
%{_libdir}/%{opera_chan}/lib_extra/libffmpeg.so

%changelog
* Wed Apr 05 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:57.0.2987.133-1
- Update to 57.0.2987.133
- Match Opera version 44.0.2510.1159

* Sat Mar 25 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:57.0.2987.98-1
- Update to 57.0.2987.98
- Match Opera version 44.0.2510.857
- Add gcc48-compat-version-stdatomic patch

* Wed Feb 22 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:56.0.2924.87-1
- Update to 56.0.2924.87
- Match Opera version 43.0.2442.991

* Tue Feb 07 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:56.0.2924.76-1
- Update to 56.0.2924.76
- Match Opera version 43.0.2442.806

* Sun Dec 25 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:55.0.2883.87-2
- Add 'depot_tools.git-master.tar.gz' into git-repo and bump version

* Sat Dec 24 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:55.0.2883.87-1
- Rework *.spec file
- Update to 55.0.2883.87
- Match Opera version 42.0.2393.94

* Tue Oct 25 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:54.0.2840.59-1
- Update to 54.0.2840.59
- Match Opera version 41.0.2353.46

* Tue Oct 18 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:53.0.2785.143-1
- Update to 53.0.2785.143
- Match Opera version 40.0.2308.90

* Tue Sep 20 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:53.0.2785.116-1
- Update to 53.0.2785.116
- Match Opera version 40.0.2308.81

* Tue Sep 20 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:53.0.2785.101-1
- Update to 53.0.2785.101
- Match Opera version 40.0.2308.54

* Tue Sep 06 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:52.0.2743.116-1
- Update to 52.0.2743.116
- Match Opera version 39.0.2256.71

* Wed Aug 03 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:52.0.2743.82-1
- Update to 52.0.2743.82
- Match Opera version 39.0.2256.43

* Fri Jul 29 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- Remove BR: faac-devel

* Mon Jul 04 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:51.0.2704.106-1
- Update to 51.0.2704.106
- Match Opera version 38.0.2220.41

* Tue Jun 14 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:51.0.2704.84-1
- Update to 51.0.2704.84
- Match Opera version 38.0.2220.31

* Tue Jun 07 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:51.0.2704.63-1
- Update to 51.0.2704.63
- Match Opera version 38.0.2220.29

* Fri Jun 03 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2661.102-2
- Switch on x86_64 arch

* Fri Jun 03 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2661.102-1
- Update to 50.0.2661.102
- Match Opera version 37.0.2178.54

* Mon May 09 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2661.94-1
- Update to 50.0.2661.94
- Match Opera version 37.0.2178.43

* Wed May 04 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:50.0.2661.87-1
- Update to 50.0.2661.87
- Match Opera version 37.0.2178.32

* Tue Apr 12 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2623.110-1
- Update to 49.0.2623.110
- Match Opera version 36.0.2130.65

* Thu Mar 31 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2623.87-1
- Update to 49.0.2623.87
- Match Opera version 36.0.2130.46

* Mon Mar 14 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:49.0.2623.75-1
- Update to 49.0.2623.75
- Match Opera version 36.0.2130.32

* Mon Feb 22 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:48.0.2564.116-1
- Update to 48.0.2564.116
- Match Opera version 35.0.2066.82
- Clean up *.spec file

* Tue Feb 16 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:48.0.2564.109-1
- Update to 48.0.2564.109
- Match Opera version 35.0.2066.68

* Mon Feb 01 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:48.0.2564.82-1
- Change package numeration due to Chromium version
- Match Opera version 35.0.2066.37
- Clip chromium source archive

* Tue Jan 19 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2036.50-1
- Update to 34.0.2036.50

* Tue Jan 12 2016 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2036.47-1
- Update to 34.0.2036.47

* Sat Dec 12 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:34.0.2036.25-1
- Update to 34.0.2036.25

* Mon Nov 30 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1990.137-1
- Update to 33.0.1990.137

* Tue Nov 17 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1990.115-1
- Update to 33.0.1990.115

* Mon Nov 02 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1990.58-1
- Update to 33.0.1990.58

* Wed Oct 28 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:33.0.1990.43-1
- Update to 33.0.1990.43

* Mon Sep 28 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> 5:32.0.1948.69-1.R
- Update to 32.0.1948.69

* Tue Sep 15 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> 5:32.0.1948.25-1.R
- Update to 32.0.1948.25

* Sat Aug 22 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru>
- Rework patch

* Fri Aug 21 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> 5:31.0.1889.174-2.R
- Drop empty debuginfo package (affects Fedora >= 24)

* Thu Aug 20 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> 5:31.0.1889.174-1.R
- Update to 31.0.1889.174
- Add check_chromium_version.sh

* Wed Aug 12 2015 carasin berlogue <carasin DOT berlogue AT mail DOT ru> 5:31.0.1889.99-1.R
- Initial build
