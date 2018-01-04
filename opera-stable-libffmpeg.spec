# NEVER EVER EVER turn this on in official builds
%global freeworld 1

# Leave this alone, please.
%global target out/Release
%global headlesstarget out/Headless

# Debuginfo packages aren't very useful here. If you need to debug
# you should do a proper debug build (not implemented in this spec yet)
%global debug_package %{nil}

# %%{nil} for Stable; -beta for Beta; -dev for Devel
# dash in -beta and -dev is intentional !
%global chromium_channel %{nil}
%global chromium_menu_name Chromium
%global chromium_browser_channel chromium-browser%{chromium_channel}
%global chromium_path %{_libdir}/chromium-browser%{chromium_channel}
%global crd_path %{_libdir}/chrome-remote-desktop

# We don't want any libs in these directories to generate Provides
# Requires is trickier.

%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so
%global privlibs libaccessibility|libaura_extra|libaura|libbase_i18n|libbase|libblink_common|libblink_core|libblink_modules|libblink_platform|libblink_web|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture|libcc_blink|libcc_ipc|libcc_proto|libcc|libcc_surfaces|libchromium_sqlite3|libcloud_policy_proto_generated_compile|libcloud_policy_proto|libcommon|libcompositor|libcontent|libcrcrypto|libdbus|libdevice_battery|libdevice_core|libdevice_event_log|libdevice_gamepad|libdevice_geolocation|libdevices|libdevice_vibration|libdisplay_compositor|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libevents_base|libevents_devices_x11|libevents_ipc|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfont_service_library|libgcm|libgeometry|libgesture_detection|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_x11|libgin|libgles2_c_lib|libgles2_implementation|libgles2_utils|libGLESv2|libgl_init|libgl_wrapper|libgpu|libgtk2ui|libicui18n|libicuuc|libipc|libkeyboard|libkeyboard_with_content|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libmedia_blink|libmedia_gpu|libmedia|libmemory_coordinator_browser|libmemory_coordinator_child|libmemory_coordinator_common|libmessage_center|libmidi|libmojo_blink_lib|libmojo_common_lib|libmojo_ime_lib|libmojo_public_system|libmojo_system_impl|libnative_theme|libnet|libnet_with_v8|libonc|libplatform|libpolicy_component|libpolicy_proto|libpower_save_blocker|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|librange|libsandbox_services|libseccomp_bpf|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing|libtranslator|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_library|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_prefs|libv8|libviews|libwebdata_common|libweb_dialogs|libwebview|libwidevinecdm|libwm|libwtf|libx11_events_platform|libx11_window|libbindings|libgeolocation|libmojo_public_system_cpp|libtime_zone_monitor|libdevice_base|libcc_animation|libcpp|libdevice_base|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libgeneric_sensor|libgl_in_process_context|libjs|libpower_monitor|libv8_libbase|libsensors|libdevice_vr|libcc_paint|libgtk3ui|libcapture_base|libcapture_lib|libfingerprint|libanimation|libcc_base|libcc_debug|libcodec|libcolor_space|libembedder|libgeometry_skia|libgin_features|libmedia_mojo_services|libplatform_wtf|libprotobuf_globals|libcdm_manager|libframe_sinks|libresource_coordinator_cpp|libblink_android_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libcontent_common_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libgeneric_sensor_public_interfaces_shared|libheadless|libipc_mojom|libipc_mojom_shared|libpublic|libresource_coordinator_public_interfaces_internal_shared|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom|libservice_manager_mojom_constants|libservice_manager_mojom_constants_shared|libservice_manager_mojom_shared|libgfx_switches|libmetrics_cpp|libui_devtools|libviz_common|libwm_public|libblink_controller|libcontent_public_common_mojo_bindings_shared|libgfx_switches|libhost|libinterfaces_shared|libmetrics_cpp|libservice|libviz_common|libwm_public|libviz_resource_format|libembedder_switches|libfreetype_harfbuzz|libmessage_support|libsandbox|libclient
%global __requires_exclude ^(%{privlibs})\\.so

# If we build with shared on, then chrome-remote-desktop depends on chromium libs.
# If we build with shared off, then users cannot swap out libffmpeg (and i686 gets a lot harder to build)
%global shared 1
# We should not need to turn this on. The app in the webstore _should_ work.
%global build_remoting_app 0

# Build Chrome Remote Desktop
%global build_remote_desktop 1

# AddressSanitizer mode
# https://www.chromium.org/developers/testing/addresssanitizer
%global asan 0

# nacl/pnacl are soon to be dead. We're just killing them off early.
%global killnacl 1

%if 0%{?killnacl}
 %global nacl 0
 %global nonacl 1
%else
# TODO: Try arm (nacl disabled)
%if 0%{?fedora}
 %ifarch i686
 %global nacl 0
 %global nonacl 1
 %else
 %global nacl 1
 %global nonacl 0
 %endif
%endif
%endif

%if 0
# Chromium's fork of ICU is now something we can't unbundle.
# This is left here to ease the change if that ever switches.
BuildRequires:  libicu-devel >= 5.4
%global bundleicu 0
%else
%global bundleicu 1
%endif

%global bundlere2 1

# The libxml_utils code depends on the specific bundled libxml checkout
# which is not compatible with the current code in the Fedora package as of
# 2017-06-08.
%global bundlelibxml 1

# Chromium breaks on wayland, hidpi, and colors with gtk3 enabled.
%global gtk3 1

%if 0%{?rhel} == 7
%global bundleopus 1
%global bundlejinja2 1
%global bundlelibusbx 1
%global bundleharfbuzz 1
%global bundlelibwebp 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%else
%global bundleharfbuzz 0
%global bundlejinja2 1
%global bundleopus 1
%global bundlelibusbx 1
%global bundlelibwebp 0
%global bundlelibpng 0
%global bundlelibjpeg 0
%endif

# Needs at least harfbuzz 1.5.0 now.
# 2017-06-12
%if 0%{?fedora} < 28
%global bundleharfbuzz 1
%else
%global bundleharfbuzz 0
%endif

### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromoting_client_id 449907151817-8vnlfih032ni8c4jjps9int9t86k546t.apps.googleusercontent.com

%global build_for_x86_64 1
%global build_for_i386 0
%define opera_chan opera-stable
%define opera_ver 50.0.2762.45

Name:		%{opera_chan}-libffmpeg
Version:	63.0.3239.108
%if 0%{?rhel} == 7
Release:	1%{?dist}
%else
Release:	1%{?dist}.R
%endif
Epoch:		5
Summary:	Additional FFmpeg library for Opera Web browser providing H264 and MP4 support
Group:		Applications/Internet
Url:		https://gist.github.com/lukaszzek/ec04d5c953226c062dac
License:	BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)

### Chromium Fedora Patches ###
#Patch1:		chromium-45.0.2454.101-linux-path-max.patch
#Patch2:		chromium-55.0.2883.75-addrfix.patch
# Google patched their bundled copy of icu 54 to include API functionality that wasn't added until 55.
# :P
#Patch4:		chromium-46.0.2490.71-notest.patch
# Ignore broken nacl open fd counter
#Patch7:		chromium-47.0.2526.80-nacl-ignore-broken-fd-counter.patch
# Use libusb_interrupt_event_handler from current libusbx (1.0.21-0.1.git448584a)
#Patch9:		chromium-48.0.2564.116-libusb_interrupt_event_handler.patch
# Use PIE in the Linux sandbox (from openSUSE via Russian Fedora)
#Patch15:	chromium-55.0.2883.75-sandbox-pie.patch
# Enable ARM CPU detection for webrtc (from archlinux via Russian Fedora)
#Patch16:	chromium-52.0.2743.82-arm-webrtc.patch
# Do not force -m32 in icu compile on ARM (from archlinux via Russian Fedora)
#Patch17:	chromium-56.0.2924.59-arm-icu-fix.patch
# Use /etc/chromium for master_prefs
#Patch18:	chromium-52.0.2743.82-master-prefs-path.patch
# Fix last commit position issue
# https://groups.google.com/a/chromium.org/forum/#!topic/gn-dev/7nlJv486bD4
Patch21:	chromium-60.0.3112.7-last-commit-position.patch
# Fix issue where timespec is not defined when sys/stat.h is included.
#Patch22:	chromium-53.0.2785.92-boringssl-time-fix.patch
# Fix gn build on Linux
# I wouldn't have to do this if there was a standard way to append extra compiler flags
Patch24:	chromium-59.0.3071.29-nullfix.patch
# Add explicit includedir for jpeglib.h
#Patch25:	chromium-54.0.2840.59-jpeg-include-dir.patch
# On i686, pass --no-keep-memory --reduce-memory-overheads to ld.
Patch26:	chromium-59.0.3071.29-i686-ld-memory-tricks.patch
# obj/content/renderer/renderer/child_frame_compositing_helper.o: In function `content::ChildFrameCompositingHelper::OnSetSurface(cc::SurfaceId const&, gfx::Size const&, float, cc::SurfaceSequence const&)':
# /builddir/build/BUILD/chromium-54.0.2840.90/out/Release/../../content/renderer/child_frame_compositing_helper.cc:214: undefined reference to `cc_blink::WebLayerImpl::setOpaque(bool)'
Patch27:	chromium-63.0.3239.70-setopaque.patch
# Use -fpermissive to build WebKit
#Patch31:	chromium-56.0.2924.87-fpermissive.patch
# Fix issue with compilation on gcc7
# Thanks to Ben Noordhuis
Patch33:	chromium-60.0.3095.5-gcc7.patch
# Revert https://chromium.googlesource.com/chromium/src/+/b794998819088f76b4cf44c8db6940240c563cf4%5E%21/#F0
# https://bugs.chromium.org/p/chromium/issues/detail?id=712737
# https://bugzilla.redhat.com/show_bug.cgi?id=1446851
Patch36:       chromium-58.0.3029.96-revert-b794998819088f76b4cf44c8db6940240c563cf4.patch
# Change struct ucontext to ucontext_t in breakpad
# https://patchwork.openembedded.org/patch/141358/
#Patch40:	chromium-59.0.3071.115-ucontext-fix.patch
# Do not prefix libpng functions
#Patch42:       chromium-60.0.3112.78-no-libpng-prefix.patch
# Do not mangle libjpeg
#Patch43:       chromium-60.0.3112.78-jpeg-nomangle.patch
# Do not mangle zlib
#Patch45:        chromium-60.0.3112.78-no-zlib-mangle.patch
# Apply this change to work around EPEL7 compiler issues
#Patch46:        chromium-62.0.3202.45-kmaxskip-constexpr.patch
#Patch47:        chromium-60.0.3112.90-vulkan-force-c99.patch
# more gcc fixes
# https://chromium.googlesource.com/chromium/src.git/+/cbe6845263215e0f3981c2a4c7937dadb14bef0d%5E%21/#F0
#Patch52:	chromium-61.0.3163.79-MOAR-GCC-FIXES.patch
# from gentoo
#Patch53:	chromium-61.0.3163.79-gcc-no-opt-safe-math.patch
# More gcc fixes for epel
#Patch54:        chromium-gcc5-r3.patch
#Patch58:	chromium-61.0.3163.79-dde535-gcc-fix.patch
#Patch59:	chromium-62.0.3202.45-gcc-nc.patch
# Epel compiler really does not like assigning nullptr to a StructPtr
#Patch60:	chromium-62.0.3202.62-epel7-no-nullptr-assignment-on-StructPtr.patch
# Another gcc 4.8 goods..
#Patch61:	chromium-62.0.3202.45-rvalue-fix.patch
# Webrtc gentto patch 
# ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-webrtc-r0.patch
#Patch62:	chromium-webrtc-r0.patch
#Patch63:	chromium-63.0.3289.84-nolibc++.patch
Patch64:	chromium-63.0.3289.84-fix-ft-hb-unbundle.patch

### Russian Fedora Patches ###
# gentoo patch ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-gn-bootstrap-r17.patch
Patch500:	chromium-gn-bootstrap-r17.patch
#Patch501:	chromium-62.0.3202.52-crc32c-iso.patch
# Clang Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-clang-r1.patch
Patch502:	chromium-clang-r1.patch

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium Fedora use chromium-latest.py --stable --ffmpegclean --ffmpegarm
# If you want to include the ffmpeg arm sources append the --ffmpegarm switch
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%%{version}.tar.xz
%if %{freeworld}
Source0:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
#%else
#Source0:	chromium-%{version}-clean.tar.xz
%endif
#Source3:	chromium-browser.sh
#Source4:	%{chromium_browser_channel}.desktop
# Also, only used if you want to reproduce the clean tarball.
#Source5:	clean_ffmpeg.sh
#Source6:	chromium-latest.py
#Source7:	get_free_ffmpeg_source_files.py
# Get the names of all tests (gtests) for Linux
# Usage: get_linux_tests_name.py chromium-%%{version} --spec
#Source8:	get_linux_tests_names.py
# GNOME stuff
#Source9:	chromium-browser.xml
#Source11:	chrome-remote-desktop@.service
#Source13:	master_preferences

# We can assume gcc and binutils.
BuildRequires:	gcc-c++

%if 0%{?asan}
BuildRequires:	clang
BuildRequires:	llvm
%endif

BuildRequires:	alsa-lib-devel
BuildRequires:	atk-devel
BuildRequires:	bison
BuildRequires:	cups-devel
BuildRequires:	dbus-devel
BuildRequires:	desktop-file-utils
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
BuildRequires:	libudev-devel
BuildRequires:	libusb-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXtst-devel
BuildRequires:	ninja-build >= 1.7.2
BuildRequires:	minizip-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	nodejs
BuildRequires:	nss-devel >= 3.26
BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel

# for /usr/bin/appstream-util
BuildRequires: libappstream-glib

# Fedora turns on NaCl
# NaCl needs these
BuildRequires:	libstdc++-devel, openssl-devel
%if 0%{?nacl}
BuildRequires:	nacl-gcc, nacl-binutils, nacl-newlib
BuildRequires:	nacl-arm-gcc, nacl-arm-binutils, nacl-arm-newlib
# pNaCl needs this monster
# It's possible that someday this dep will stabilize, but
# right now, it needs to be updated everytime chromium bumps
# a major version.
BuildRequires:	chromium-native_client >= 52.0.2743.82
%ifarch x86_64
# Really, this is what we want:
# BuildRequires:  glibc-devel(x86-32) libgcc(x86-32)
# But, koji only offers glibc32. Maybe that's enough.
# This BR will pull in either glibc.i686 or glibc32.
BuildRequires:	/lib/libc.so.6 /usr/lib/libc.so
%endif
%endif
# Fedora tries to use system libs whenever it can.
BuildRequires:	bzip2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	elfutils-libelf-devel
BuildRequires:	flac-devel
BuildRequires:	hwdata
BuildRequires:	kernel-headers
BuildRequires:	libevent-devel
BuildRequires:	libffi-devel
BuildRequires:	vulkan-devel
%if 0%{?bundleicu}
# If this is true, we're using the bundled icu.
# We'd like to use the system icu every time, but we cannot always do that.
%else
# Not newer than 54 (at least not right now)
BuildRequires:	libicu-devel = 54.1
%endif
BuildRequires:	libjpeg-devel
%if 0%{?bundlelibpng}
# If this is true, we're using the bundled libpng
# which we need to do because the RHEL 7 libpng doesn't work right anymore
%else
BuildRequires:	libpng-devel
%endif
%if 0
# see https://code.google.com/p/chromium/issues/detail?id=501318
BuildRequires:	libsrtp-devel >= 1.4.4
%endif
BuildRequires:	libudev-devel
%if %{bundlelibusbx}
# Do nothing
%else
Requires:	libusbx >= 1.0.21-0.1.git448584a
BuildRequires:	libusbx-devel >= 1.0.21-0.1.git448584a
%endif
# We don't use libvpx anymore because Chromium loves to
# use bleeding edge revisions here that break other things
# ... so we just use the bundled libvpx.
%if %{bundlelibwebp}
# Do nothing
%else
BuildRequires:	libwebp-devel
%endif
BuildRequires:	libxslt-devel
# Same here, it seems.
# BuildRequires:	libyuv-devel
%if %{bundleopus}
# Do nothing
%else
BuildRequires:	opus-devel
%endif
BuildRequires:	perl(Switch)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	python2
BuildRequires:	python-beautifulsoup4
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-html5lib
%if 0%{?bundlejinja2}
# Using bundled bits, do nothing.
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
BuildRequires:	speech-dispatcher-devel
BuildRequires:	yasm
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(gnome-keyring-1)
# remote desktop needs this
BuildRequires:	pam-devel
BuildRequires:	systemd

%if 0%{?rhel} == 7
BuildRequires: devtoolset-7-toolchain, devtoolset-7-libatomic-devel
%endif

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
%setup -q -n chromium-%{version}

# Fix Russian Translation
sed -i 's@адежный@адёжный@g' components/strings/components_strings_ru.xtb

# fix debugedit: canonicalization unexpectedly shrank by one character
sed -i 's@gpu//@gpu/@g' content/renderer/gpu/compositor_forwarding_message_filter.cc
sed -i 's@audio_processing//@audio_processing/@g' third_party/webrtc/modules/audio_processing/utility/ooura_fft.cc
sed -i 's@audio_processing//@audio_processing/@g' third_party/webrtc/modules/audio_processing/utility/ooura_fft_sse2.cc

### Chromium Fedora Patches ###
#%patch1 -p1 -b .pathmax
#%patch2 -p1 -b .addrfix
#%patch4 -p1 -b .notest
#%patch7 -p1 -b .ignore-fd-count
#%patch9 -p1 -b .modern-libusbx
#%patch15 -b .sandboxpie
#%patch16 -p1 -b .armwebrtc
#%patch17 -p1 -b .armfix
#%patch18 -p1 -b .etc
%patch21 -p1 -b .lastcommit
#%patch22 -p1 -b .timefix
%patch24 -p1 -b .nullfix
#%patch25 -p1 -b .jpegfix
%patch26 -p1 -b .ldmemory
%patch27 -p1 -b .setopaque
#%patch31 -p1 -b .permissive
#%patch33 -p1 -b .gcc7
%patch36 -p1 -b .revert
#%patch40 -p1 -b .ucontextfix
#%patch42 -p1 -b .noprefix
#%patch43 -p1 -b .nomangle
#%patch45 -p1 -b .nozmangle
#%if 0%{?rhel} == 7
#%patch46 -p1 -b .kmaxskip
#%patch47 -p1 -b .c99
#%patch54 -p1 -b .gcc5fix
#%patch58 -p1 -b .dde5e35
#%patch59 -p1 -b .gcc-nc
#%patch60 -p1 -b .nonullptr
#%patch61 -p1 -b .another-rvalue-fix
#%endif

#%patch62 -p1 -b .webrtc
#%patch63 -p1 -b .nolibc++
%patch64 -p1 -b .ft-hb

#%patch52 -p1 -b .fixgccagain
#%patch53 -p1 -b .nogccoptmath

### Russian Fedora Patches ###
#%patch500 -p1 -b .gn-bootstrap-r8
#%patch501 -p1 -b .std++17


%if 0%{?asan}
%patch502 -p1 -b .clang
export CC="clang"
export CXX="clang++"
%else
export CC="gcc"
export CXX="g++"
%endif
export AR="ar"
export RANLIB="ranlib"

# NUKE FROM ORBIT
#rm -rf buildtools/third_party/libc++/BUILD.gn

%if 0%{?nacl}
# prep the nacl tree
mkdir -p out/Release/gen/sdk/linux_x86/nacl_x86_newlib
cp -a --no-preserve=context /usr/%{_arch}-nacl/* out/Release/gen/sdk/linux_x86/nacl_x86_newlib

mkdir -p out/Release/gen/sdk/linux_x86/nacl_arm_newlib
cp -a --no-preserve=context /usr/arm-nacl/* out/Release/gen/sdk/linux_x86/nacl_arm_newlib

# Not sure if we need this or not, but better safe than sorry.
pushd out/Release/gen/sdk/linux_x86
ln -s nacl_x86_newlib nacl_x86_newlib_raw
ln -s nacl_arm_newlib nacl_arm_newlib_raw
popd

mkdir -p out/Release/gen/sdk/linux_x86/nacl_x86_newlib/bin
pushd out/Release/gen/sdk/linux_x86/nacl_x86_newlib/bin
ln -s /usr/bin/x86_64-nacl-gcc gcc
ln -s /usr/bin/x86_64-nacl-gcc x86_64-nacl-gcc
ln -s /usr/bin/x86_64-nacl-g++ g++
ln -s /usr/bin/x86_64-nacl-g++ x86_64-nacl-g++
# ln -s /usr/bin/x86_64-nacl-ar ar
ln -s /usr/bin/x86_64-nacl-ar x86_64-nacl-ar
# ln -s /usr/bin/x86_64-nacl-as as
ln -s /usr/bin/x86_64-nacl-as x86_64-nacl-as
# ln -s /usr/bin/x86_64-nacl-ranlib ranlib
ln -s /usr/bin/x86_64-nacl-ranlib x86_64-nacl-ranlib
# Cleanups
rm addr2line
ln -s /usr/bin/x86_64-nacl-addr2line addr2line
rm c++filt
ln -s /usr/bin/x86_64-nacl-c++filt c++filt
rm gprof
ln -s /usr/bin/x86_64-nacl-gprof gprof
rm readelf
ln -s /usr/bin/x86_64-nacl-readelf readelf
rm size
ln -s /usr/bin/x86_64-nacl-size size
rm strings
ln -s /usr/bin/x86_64-nacl-strings strings
popd

mkdir -p out/Release/gen/sdk/linux_x86/nacl_arm_newlib/bin
pushd out/Release/gen/sdk/linux_x86/nacl_arm_newlib/bin
ln -s /usr/bin/arm-nacl-gcc gcc
ln -s /usr/bin/arm-nacl-gcc arm-nacl-gcc
ln -s /usr/bin/arm-nacl-g++ g++
ln -s /usr/bin/arm-nacl-g++ arm-nacl-g++
ln -s /usr/bin/arm-nacl-ar arm-nacl-ar
ln -s /usr/bin/arm-nacl-as arm-nacl-as
ln -s /usr/bin/arm-nacl-ranlib arm-nacl-ranlib
popd

touch out/Release/gen/sdk/linux_x86/nacl_x86_newlib/stamp.untar out/Release/gen/sdk/linux_x86/nacl_x86_newlib/stamp.prep
touch out/Release/gen/sdk/linux_x86/nacl_x86_newlib/nacl_x86_newlib.json
touch out/Release/gen/sdk/linux_x86/nacl_arm_newlib/stamp.untar out/Release/gen/sdk/linux_x86/nacl_arm_newlib/stamp.prep
touch out/Release/gen/sdk/linux_x86/nacl_arm_newlib/nacl_arm_newlib.json

pushd out/Release/gen/sdk/linux_x86/
mkdir -p pnacl_newlib pnacl_translator
# Might be able to do symlinks here, but eh.
cp -a --no-preserve=context /usr/pnacl_newlib/* pnacl_newlib/
cp -a --no-preserve=context /usr/pnacl_translator/* pnacl_translator/
for i in lib/libc.a lib/libc++.a lib/libg.a lib/libm.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/x86_64_bc-nacl/$i
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/i686_bc-nacl/$i
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/le32-nacl/$i
done

for i in lib/libpthread.a lib/libnacl.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/le32-nacl/$i
done

for i in lib/clang/3.7.0/lib/x86_64_bc-nacl/libpnaclmm.a lib/clang/3.7.0/lib/i686_bc-nacl/libpnaclmm.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/$i
done

for i in lib/clang/3.7.0/lib/le32-nacl/libpnaclmm.a lib/clang/3.7.0/lib/le32-nacl/libgcc.a; do
	/usr/pnacl_newlib/bin/pnacl-ranlib pnacl_newlib/$i
done

popd

mkdir -p native_client/toolchain/.tars/linux_x86
touch native_client/toolchain/.tars/linux_x86/pnacl_translator.json

pushd native_client/toolchain
ln -s ../../out/Release/gen/sdk/linux_x86 linux_x86
popd

mkdir -p third_party/llvm-build/Release+Asserts/bin
pushd third_party/llvm-build/Release+Asserts/bin
ln -sf /usr/bin/clang clang
ln -sf /usr/bin/clang++ clang++
popd
%endif

# Core defines are flags that are true for both the browser and headless.
CHROMIUM_CORE_GN_DEFINES=""
CHROMIUM_CORE_GN_DEFINES+=' is_debug=false'
%ifarch x86_64
CHROMIUM_CORE_GN_DEFINES+=' system_libdir="lib64"'
%endif
CHROMIUM_CORE_GN_DEFINES+=' google_api_key="%{api_key}" google_default_client_id="%{default_client_id}" google_default_client_secret="%{default_client_secret}"'
%if 0%{?asan}
CHROMIUM_CORE_GN_DEFINES+=' is_clang=true clang_base_path="/usr" clang_use_chrome_plugins=false fatal_linker_warnings=false use_lld=false'
%else
CHROMIUM_CORE_GN_DEFINES+=' is_clang=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' use_sysroot=false use_gold=false fieldtrial_testing_like_official_build=true  use_custom_libcxx=false'
%if %{freeworld}
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="ChromeOS" proprietary_codecs=true'
%else
CHROMIUM_CORE_GN_DEFINES+=' ffmpeg_branding="Chromium" proprietary_codecs=false'
%endif
CHROMIUM_CORE_GN_DEFINES+=' treat_warnings_as_errors=false linux_use_bundled_binutils=false use_custom_libcxx=false'
export CHROMIUM_CORE_GN_DEFINES

CHROMIUM_BROWSER_GN_DEFINES=""
CHROMIUM_BROWSER_GN_DEFINES+=' use_gio=true use_pulseaudio=true icu_use_data_file=true'
%if 0%{?nonacl}
CHROMIUM_BROWSER_GN_DEFINES+=' enable_nacl=false'
%endif
%if 0%{?shared}
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=true is_component_build=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' is_component_ffmpeg=false is_component_build=false'
%endif
CHROMIUM_BROWSER_GN_DEFINES+=' remove_webcore_debug_symbols=true enable_hangout_services_extension=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_hotwording=false use_aura=true'
CHROMIUM_BROWSER_GN_DEFINES+=' enable_webrtc=true enable_widevine=true'
%if 0%{gtk3}
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk3=true'
%else
CHROMIUM_BROWSER_GN_DEFINES+=' use_gtk3=false'
%endif
export CHROMIUM_BROWSER_GN_DEFINES

CHROMIUM_HEADLESS_GN_DEFINES=""
CHROMIUM_HEADLESS_GN_DEFINES+=' use_ozone=true ozone_auto_platforms=false ozone_platform="headless" ozone_platform_headless=true'
CHROMIUM_HEADLESS_GN_DEFINES+=' headless_use_embedded_resources=true icu_use_data_file=false v8_use_external_startup_data=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' enable_nacl=false enable_print_preview=false enable_remoting=false use_alsa=false use_ash=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_cups=false use_dbus=false use_gconf=false use_gio=false use_kerberos=false use_libpci=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_pulseaudio=false use_udev=false'
export CHROMIUM_HEADLESS_GN_DEFINES

# Remove most of the bundled libraries. Libraries specified below (taken from
# Gentoo's Chromium ebuild) are the libraries that needs to be preserved.
build/linux/unbundle/remove_bundled_libraries.py \
	'buildtools/third_party/libc++' \
	'buildtools/third_party/libc++abi' \
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
%if %{freeworld}
	'third_party/openh264' \
%endif
%if 0%{?bundlere2}
	'third_party/re2' \
%endif
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
	'third_party/angle/src/common/third_party/base' \
	'third_party/angle/src/common/third_party/smhasher' \
	'third_party/angle/src/third_party/compiler' \
	'third_party/angle/src/third_party/libXNVCtrl' \
	'third_party/angle/src/third_party/trace_event' \
	'third_party/blink' \
	'third_party/blanketjs' \
	'third_party/boringssl' \
	'third_party/breakpad' \
	'third_party/breakpad/breakpad/src/third_party/curl' \
	'third_party/brotli' \
	'third_party/cacheinvalidation' \
	'third_party/catapult' \
	'third_party/catapult/common/py_vulcanize/third_party/rcssmin' \
	'third_party/catapult/common/py_vulcanize/third_party/rjsmin' \
	'third_party/catapult/tracing/third_party/d3' \
	'third_party/catapult/tracing/third_party/gl-matrix' \
	'third_party/catapult/tracing/third_party/jszip' \
	'third_party/catapult/tracing/third_party/mannwhitneyu' \
	'third_party/catapult/tracing/third_party/oboe' \
	'third_party/catapult/tracing/third_party/pako' \
	'third_party/catapult/third_party/polymer' \
	'third_party/ced' \
	'third_party/cld_2' \
	'third_party/crc32c' \
	'third_party/cros_system_api' \
	'third_party/devscripts' \
	'third_party/dom_distiller_js' \
	'third_party/expat' \
	'third_party/fips181' \
        'third_party/flatbuffers' \
	'third_party/flot' \
	'third_party/freetype' \
	'third_party/glslang-angle' \
	'third_party/google_input_tools' \
	'third_party/google_input_tools/third_party/closure_library' \
	'third_party/google_input_tools/third_party/closure_library/third_party/closure' \
	'third_party/googletest' \
	'third_party/hunspell' \
	'third_party/libdrm' \
	'third_party/iccjpeg' \
%if 0%{?bundlejinja2}
	'third_party/jinja2' \
%endif
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
%if 0%{?nacl}
	'third_party/llvm-build' \
%endif
	'third_party/lss' \
	'third_party/lzma_sdk' \
	'third_party/mesa' \
	'third_party/modp_b64' \
	'third_party/mt19937ar' \
	'third_party/node' \
	'third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2' \
	'third_party/openmax_dl' \
	'third_party/opus' \
	'third_party/ots' \
	'third_party/pdfium' \
	'third_party/pdfium/third_party/agg23' \
	'third_party/pdfium/third_party/base' \
	'third_party/pdfium/third_party/build' \
	'third_party/pdfium/third_party/bigint' \
	'third_party/pdfium/third_party/freetype' \
	'third_party/pdfium/third_party/lcms' \
	'third_party/pdfium/third_party/libopenjpeg20' \
	'third_party/pdfium/third_party/libpng16' \
	'third_party/pdfium/third_party/libtiff' \
	'third_party/polymer' \
	'third_party/protobuf' \
	'third_party/protobuf/third_party/six' \
	'third_party/ply' \
	'third_party/qcms' \
	'third_party/qunit' \
	'third_party/sfntly' \
	'third_party/sinonjs' \
	'third_party/skia' \
	'third_party/skia/third_party/gif' \
	'third_party/skia/third_party/vulkan' \
	'third_party/smhasher' \
	'third_party/spirv-headers' \
	'third_party/spirv-tools-angle' \
	'third_party/sqlite' \
	'third_party/swiftshader' \
	'third_party/swiftshader/third_party/llvm-subzero' \
	'third_party/swiftshader/third_party/subzero' \
	'third_party/tcmalloc' \
	'third_party/usrsctp' \
	'third_party/vulkan' \
	'third_party/vulkan-validation-layers' \
	'third_party/web-animations-js' \
	'third_party/webdriver' \
	'third_party/webrtc' \
	'third_party/widevine' \
	'third_party/woff2' \
	'third_party/zlib/google' \
	'url/third_party/mozilla' \
	'v8/src/third_party/valgrind' \
	--do-remove

# Look, I don't know. This package is spit and chewing gum. Sorry.

%if ! 0%{?bundlejinja2}
rm -rf third_party/jinja2
ln -s %{python_sitelib}/jinja2 third_party/jinja2
%endif
rm -rf third_party/markupsafe
ln -s %{python_sitearch}/markupsafe third_party/markupsafe
# We should look on removing other python packages as well i.e. ply

%if %{build_remote_desktop}
# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc
%endif

export PATH=$PATH:%{_builddir}/depot_tools

build/linux/unbundle/replace_gn_files.py --system-libraries \
	flac \
	freetype \
%if 0%{?bundleharfbuzz}
%else
	harfbuzz-ng \
%endif
%if 0%{?bundleicu}
%else
	icu \
%endif
	libdrm \
%if %{bundlelibjpeg}
%else
	libjpeg \
%endif
%if %{bundlelibpng}
%else
	libpng \
%endif
%if %{bundlelibusbx}
%else
	libusb \
%endif
%if %{bundlelibwebp}
%else
	libwebp \
%endif
%if %{bundlelibxml}
%else
	libxml \
%endif
	libxslt \
%if %{bundleopus}
%else
	opus \
%endif
%if 0%{?bundlere2}
%else
	re2 \
%endif
	yasm \
	zlib

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

tools/gn/bootstrap/bootstrap.py -v --gn-gen-args "$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES"
%{target}/gn gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_BROWSER_GN_DEFINES" %{target}

%{target}/gn gen --args="$CHROMIUM_CORE_GN_DEFINES $CHROMIUM_HEADLESS_GN_DEFINES" %{headlesstarget}

%if %{bundlelibusbx}
# no hackity hack hack
%else
# hackity hack hack
rm -rf third_party/libusb/src/libusb/libusb.h
# we _shouldn't need to do this, but it looks like we do.
cp -a %{_includedir}/libusb-1.0/libusb.h third_party/libusb/src/libusb/libusb.h
%endif

# make up a version for widevine
sed '14i#define WIDEVINE_CDM_VERSION_STRING "Something fresh"' -i "third_party/widevine/cdm/stub/widevine_cdm_version.h"

# Hard code extra version
FILE=chrome/common/channel_info_posix.cc
sed -i.orig -e 's/getenv("CHROME_VERSION_EXTRA")/"Russian Fedora"/' $FILE

# fix arm gcc
sed -i 's|arm-linux-gnueabihf-|arm-linux-gnu-|g' build/toolchain/linux/BUILD.gn

# setup node
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/node

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

# Now do the full browser
# Do headless first.
#ninja -C %{headlesstarget} -vvv headless_shell

ninja -C %{target} -vvv libffmpeg.so

# Nuke nacl/pnacl bits at the end of the build
rm -rf out/Release/gen/sdk
rm -rf native_client/toolchain
rm -rf third_party/llvm-build/*

%install
mkdir -p %{buildroot}%{_libdir}/%{opera_chan}/lib_extra
install -m 644 %{_builddir}/chromium-%{version}/out/Release/libffmpeg.so %{buildroot}%{_libdir}/%{opera_chan}/lib_extra/

%files
%{_libdir}/%{opera_chan}/lib_extra/libffmpeg.so

%changelog
* Thu Jan 04 2018 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:63.0.3239.108-1
- Update to 63.0.3239.108
- Match Opera version 50.0.2762.45
- Add patches:
    chromium-63.0.3289.84-fix-ft-hb-unbundle.patch
    chromium-clang-r1.patch

* Thu Nov 16 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:62.0.3202.89-1
- Update to 62.0.3202.89
- Match Opera version 49.0.2725.39
- Add patches:
    chromium-gn-bootstrap-r17.patch
- Drop patches:
    chromium-gn-bootstrap-r14.patch
    chromium-gcc-r1.patch

* Sat Oct 21 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:59.0.3071.115-2
- Drop some unneeded deps

* Sat Oct 21 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:59.0.3071.115-1
- Update to 61.0.3163.100
- Match Opera version 48.0.2685.50
- Rework *.spec file
- Add patches:
    chromium-61.0.3163.49-setopaque.patch
    chromium-gcc-r1.patch
    chromium-gn-bootstrap-r14.patch
- Drop patches:
    chromium-59.0.3071.29-setopaque.patch
    chromium-gn-bootstrap-r8.patch

* Sun Aug 13 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:60.0.3112.78-1
- Update to 60.0.3112.78
- Match Opera version 47.0.2631.39
- Rework *.spec file
- Add patches:
    chromium-gn-bootstrap-r8.patch
    chromium-58.0.3029.96-revert-b794998819088f76b4cf44c8db6940240c563cf4.patch
    chromium-60.0.3095.5-gcc7.patch
    chromium-60.0.3112.7-last-commit-position.patch
- Drop patches:
    chromium-53.0.2785.92-last-commit-position.patch
    chromium-59.0.3071.29-gcc7.patch

* Thu Jul 06 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:59.0.3071.115-1
- Update to 59.0.3071.115
- Match Opera version 46.0.2597.39

* Wed Jun 21 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:59.0.3071.86-1
- Update to 59.0.3071.86
- Match Opera version 46.0.2597.26
- Add patches:
    chromium-59.0.3071.29-nullfix.patch
    chromium-59.0.3071.29-i686-ld-memory-tricks.patch
    chromium-59.0.3071.29-setopaque.patch
    chromium-59.0.3071.29-gcc7.patch
- Drop patches:
    chromium-57.0.2987.98-gcc48-compat-version-stdatomic.patch
    chromium-gn-bootstrap-r2.patch

* Fri May 26 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:58.0.3029.110-1
- Update to 58.0.3029.110
- Match Opera version 45.0.2552.881

* Tue May 09 2017 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:58.0.3029.81-1
- Update to 58.0.3029.81
- Match Opera version 45.0.2552.635

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
