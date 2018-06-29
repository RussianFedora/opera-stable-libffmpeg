# define python version
%global __python /usr/bin/python2

# NEVER EVER EVER turn this on in official builds
%global freeworld 1

# Some people wish not to use the Fedora Google API keys. Mmkay.
# Expect stuff to break in weird ways if you disable.
%global useapikeys 1

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

%global __provides_exclude_from %{chromium_path}/.*\\.so|%{chromium_path}/lib/.*\\.so|%{chromium_path}/lib/.*\\.so.*
%if 0%{?rhel} == 7
%global privlibs libaccessibility|libanimation|libapdu|libaura_extra|libaura|libbase_i18n|libbase|libbindings_base|libbindings|libblink_android_mojo_bindings_shared|libblink_common|libblink_controller|libblink_core_mojo_bindings_shared|libblink_core|libblink_modules|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libblink_platform|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture_base|libcapture_lib|libcbor|libcc_animation|libcc_base|libcc_blink|libcc_debug|libcc_ipc|libcc_paint|libcc|libcdm_manager|libchromium_sqlite3|libclearkeycdm|libclient|libcloud_policy_proto_generated_compile|libcodec|libcolor_space|libcommon|libcompositor|libcontent_common_mojo_bindings_shared|libcontent_public_common_mojo_bindings_shared|libcontent|libcrash_key|libcrcrypto|libdbus|libdevice_base|libdevice_event_log|libdevice_features|libdevice_gamepad|libdevices|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libembedder|libembedder_switches|libevents_base|libevents_devices_x11|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfido|libfingerprint|libfreetype_harfbuzz|libgcm|libgeolocation|libgeometry_skia|libgeometry|libgesture_detection|libgfx_ipc_buffer_types|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_switches|libgfx_x11|libgin|libgles2_implementation|libgles2|libgles2_utils|libGLESv2|libgl_init|libgl_in_process_context|libgl_wrapper|libgpu_ipc_service|libgpu|libgpu_util|libgtk3ui|libheadless|libhost|libicui18n|libicuuc|libinterfaces_shared|libipc_mojom_shared|libipc_mojom|libipc|libkeyboard|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libleveldatabase|libmanager|libmedia_blink|libmedia_devices_mojo_bindings_shared|libmedia_gpu|libmedia_mojo_services|libmedia|libmessage_center|libmessage_support|libmetrics_cpp|libmidi|libmirclient|libmojo_base_lib|libmojo_base_mojom_blink|libmojo_base_mojom_shared|libmojo_base_mojom|libmojo_base_shared_typemap_traits|libmojo_edk_ports|libmojo_edk|libmojo_ime_lib|libmojom_core_shared|libmojo_mojom_bindings_shared|libmojo_mojom_bindings|libmojom_platform_shared|libmojo_public_system_cpp|libmojo_public_system|libnative_theme|libnet|libnet_with_v8|libnetwork_cpp_base|libnetwork_cpp|libnetwork_service|libnetwork_session_configurator|libonc|libplatform|libpolicy_component|libpolicy_proto|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|libpublic|librange|libraster|libresource_coordinator_cpp_base|libresource_coordinator_cpp|libresource_coordinator_public_mojom_blink|libresource_coordinator_public_mojom_shared|libresource_coordinator_public_mojom|libsandbox_services|libsandbox|libseccomp_bpf|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom_blink|libservice_manager_mojom_constants_blink|libservice_manager_mojom_constants_shared|libservice_manager_mojom_constants|libservice_manager_mojom_shared|libservice_manager_mojom|libservice|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing_cpp|libtracing_mojom_shared|libtracing_mojom|libtracing|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_devtools|libui_message_center_cpp|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_manager|libuser_prefs|libv8_libbase|libv8_libplatform|libv8|libviews|libviz_common|libviz_resource_format|libVkLayer_core_validation|libVkLayer_object_tracker|libVkLayer_parameter_validation|libVkLayer_threading|libVkLayer_unique_objects|libwebdata_common|libweb_dialogs|libwebview|libwm_public|libwm|libwtf|libx11_events_platform|libx11_window|libbase|libEGL|libGLESv2|libfontconfig
%else
%global privlibs libaccessibility|libanimation|libapdu|libaura_extra|libaura|libbase_i18n|libbase|libbindings_base|libbindings|libblink_android_mojo_bindings_shared|libblink_common|libblink_controller|libblink_core_mojo_bindings_shared|libblink_core|libblink_modules|libblink_mojo_bindings_shared|libblink_offscreen_canvas_mojo_bindings_shared|libblink_platform|libbluetooth|libboringssl|libbrowser_ui_views|libcaptive_portal|libcapture_base|libcapture_lib|libcbor|libcc_animation|libcc_base|libcc_blink|libcc_debug|libcc_ipc|libcc_paint|libcc|libcdm_manager|libchromium_sqlite3|libclearkeycdm|libclient|libcloud_policy_proto_generated_compile|libcodec|libcolor_space|libcommon|libcompositor|libcontent_common_mojo_bindings_shared|libcontent_public_common_mojo_bindings_shared|libcontent|libcrash_key|libcrcrypto|libdbus|libdevice_base|libdevice_event_log|libdevice_features|libdevice_gamepad|libdevices|libdevice_vr_mojo_bindings_blink|libdevice_vr_mojo_bindings_shared|libdevice_vr_mojo_bindings|libdevice_vr|libdiscardable_memory_client|libdiscardable_memory_common|libdiscardable_memory_service|libdisplay|libdisplay_types|libdisplay_util|libdomain_reliability|libEGL|libembedder|libembedder_switches|libevents_base|libevents_devices_x11|libevents_ozone_layout|libevents|libevents_x|libffmpeg|libfido|libfingerprint|libfreetype_harfbuzz|libgcm|libgeolocation|libgeometry_skia|libgeometry|libgesture_detection|libgfx_ipc_buffer_types|libgfx_ipc_color|libgfx_ipc_geometry|libgfx_ipc_skia|libgfx_ipc|libgfx|libgfx_switches|libgfx_x11|libgin|libgles2_implementation|libgles2|libgles2_utils|libGLESv2|libgl_init|libgl_in_process_context|libgl_wrapper|libgpu_ipc_service|libgpu|libgpu_util|libgtk3ui|libheadless|libhost|libicui18n|libicuuc|libinterfaces_shared|libipc_mojom_shared|libipc_mojom|libipc|libkeyboard|libkeycodes_x11|libkeyed_service_content|libkeyed_service_core|libleveldatabase|libmanager|libmedia_blink|libmedia_devices_mojo_bindings_shared|libmedia_gpu|libmedia_mojo_services|libmedia|libmessage_center|libmessage_support|libmetrics_cpp|libmidi|libmirclient|libmojo_base_lib|libmojo_base_mojom_blink|libmojo_base_mojom_shared|libmojo_base_mojom|libmojo_base_shared_typemap_traits|libmojo_edk_ports|libmojo_edk|libmojo_ime_lib|libmojom_core_shared|libmojo_mojom_bindings_shared|libmojo_mojom_bindings|libmojom_platform_shared|libmojo_public_system_cpp|libmojo_public_system|libnative_theme|libnet|libnet_with_v8|libnetwork_cpp_base|libnetwork_cpp|libnetwork_service|libnetwork_session_configurator|libonc|libplatform|libpolicy_component|libpolicy_proto|libppapi_host|libppapi_proxy|libppapi_shared|libprefs|libprinting|libprotobuf_lite|libproxy_config|libpublic|librange|libraster|libresource_coordinator_cpp_base|libresource_coordinator_cpp|libresource_coordinator_public_mojom_blink|libresource_coordinator_public_mojom_shared|libresource_coordinator_public_mojom|libsandbox_services|libsandbox|libseccomp_bpf|libservice_manager_cpp|libservice_manager_cpp_types|libservice_manager_mojom_blink|libservice_manager_mojom_constants_blink|libservice_manager_mojom_constants_shared|libservice_manager_mojom_constants|libservice_manager_mojom_shared|libservice_manager_mojom|libservice|libsessions|libshared_memory_support|libshell_dialogs|libskia|libsnapshot|libsql|libstartup_tracing|libstorage_browser|libstorage_common|libstub_window|libsuid_sandbox_client|libsurface|libtracing_cpp|libtracing_mojom_shared|libtracing_mojom|libtracing|libui_base_ime|libui_base|libui_base_x|libui_data_pack|libui_devtools|libui_message_center_cpp|libui_touch_selection|libui_views_mus_lib|liburl_ipc|liburl_matcher|liburl|libuser_manager|libuser_prefs|libv8_libbase|libv8_libplatform|libv8|libviews|libviz_common|libviz_resource_format|libVkLayer_core_validation|libVkLayer_object_tracker|libVkLayer_parameter_validation|libVkLayer_threading|libVkLayer_unique_objects|libwebdata_common|libweb_dialogs|libwebview|libwm_public|libwm|libwtf|libx11_events_platform|libx11_window|libbase|libEGL|libGLESv2
%endif
%global __requires_exclude ^(%{privlibs})\\.so*

# If we build with shared on, then chrome-remote-desktop depends on chromium libs.
# If we build with shared off, then users cannot swap out libffmpeg (and i686 gets a lot harder to build)
%global shared 1
# We should not need to turn this on. The app in the webstore _should_ work.
%global build_remoting_app 0

# Build Chrome Remote Desktop
%global build_remote_desktop 1

# AddressSanitizer mode
# https://www.chromium.org/developers/testing/addresssanitizer
#%if 0%%{?fedora} >= 28
#%%global asan 1
#%else
%global asan 0
#%endif

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

# Chromium used to break on wayland, hidpi, and colors with gtk3 enabled.
# Hopefully it does not anymore.
%global gtk3 1

# Enable vaapi
%global vaapi 0

%if 0%{?rhel} == 7
%global bundleopus 1
%global bundlelibusbx 1
%global bundleharfbuzz 1
%global bundlelibwebp 1
%global bundlelibpng 1
%global bundlelibjpeg 1
%global bundlefreetype 1
%global bundlelibdrm 1
%global bundlefontconfig 1
%else
%global bundleharfbuzz 0
%global bundleopus 1
%global bundlelibusbx 1
%global bundlelibwebp 0
%global bundlelibpng 0
%global bundlelibjpeg 0
%global bundlefreetype 0
%global bundlelibdrm 0
%global bundlefontconfig 0
%endif

# Needs at least harfbuzz 1.7.3 now.
# 2018-03-07
%if 0%{?fedora} < 28
%global bundleharfbuzz 1
%else
%global bundleharfbuzz 0
%endif

### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%if %{useapikeys}
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
%global chromoting_client_id 449907151817-8vnlfih032ni8c4jjps9int9t86k546t.apps.googleusercontent.com
%else
%global api_key %nil
%global default_client_id %nil
%global default_client_secret %nil
%global chromoting_client_id %nil
%endif

%global build_for_x86_64 1
%global build_for_i386 0
%define opera_chan opera-stable
%define opera_ver 54.0.2952.41

Name:		%{opera_chan}-libffmpeg
Version:	67.0.3396.87
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
Patch0:		chromium-67.0.3396.62-gcc5.patch
#Patch1:		chromium-45.0.2454.101-linux-path-max.patch
#Patch2:		chromium-55.0.2883.75-addrfix.patch
#Patch4:		chromium-46.0.2490.71-notest.patch
# In file included from ../linux/directory.c:21:
# In file included from ../../../../native_client/src/nonsfi/linux/abi_conversion.h:20:
# ../../../../native_client/src/nonsfi/linux/linux_syscall_structs.h:44:13: error: GNU-style inline assembly is disabled
#     __asm__ __volatile__("mov %%gs, %0" : "=r"(gs));
#             ^
# 1 error generated.
#Patch6:		chromium-47.0.2526.80-pnacl-fgnu-inline-asm.patch
# Ignore broken nacl open fd counter
#Patch7:		chromium-47.0.2526.80-nacl-ignore-broken-fd-counter.patch
# Use libusb_interrupt_event_handler from current libusbx (1.0.21-0.1.git448584a)
#Patch9:		chromium-48.0.2564.116-libusb_interrupt_event_handler.patch
# Ignore deprecations in cups 2.2
# https://bugs.chromium.org/p/chromium/issues/detail?id=622493
#Patch12:	chromium-55.0.2883.75-cups22.patch
# Use PIE in the Linux sandbox (from openSUSE via Russian Fedora)
#Patch15:	chromium-55.0.2883.75-sandbox-pie.patch
# Use /etc/chromium for master_prefs
#Patch18:	chromium-52.0.2743.82-master-prefs-path.patch
# Disable MADV_FREE (if set by glibc)
# https://bugzilla.redhat.com/show_bug.cgi?id=1361157
#Patch19:	chromium-52.0.2743.116-unset-madv_free.patch
# Use gn system files
#Patch20:	chromium-67.0.3396.62-gn-system.patch
# Fix last commit position issue
# https://groups.google.com/a/chromium.org/forum/#!topic/gn-dev/7nlJv486bD4
Patch21:	chromium-60.0.3112.78-last-commit-position.patch
# Fix issue where timespec is not defined when sys/stat.h is included.
#Patch22:	chromium-53.0.2785.92-boringssl-time-fix.patch
# I wouldn't have to do this if there was a standard way to append extra compiler flags
Patch24:	chromium-63.0.3289.84-nullfix.patch
# Add explicit includedir for jpeglib.h
#Patch25:	chromium-54.0.2840.59-jpeg-include-dir.patch
# On i686, pass --no-keep-memory --reduce-memory-overheads to ld.
Patch26:	chromium-59.0.3071.86-i686-ld-memory-tricks.patch
# obj/content/renderer/renderer/child_frame_compositing_helper.o: In function `content::ChildFrameCompositingHelper::OnSetSurface(cc::SurfaceId const&, gfx::Size const&, float, cc::SurfaceSequence const&)':
# /builddir/build/BUILD/chromium-54.0.2840.90/out/Release/../../content/renderer/child_frame_compositing_helper.cc:214: undefined reference to `cc_blink::WebLayerImpl::setOpaque(bool)'
Patch27:	chromium-63.0.3289.84-setopaque.patch
# Revert https://chromium.googlesource.com/chromium/src/+/b794998819088f76b4cf44c8db6940240c563cf4%5E%21/#F0
# https://bugs.chromium.org/p/chromium/issues/detail?id=712737
# https://bugzilla.redhat.com/show_bug.cgi?id=1446851
Patch36:	chromium-58.0.3029.96-revert-b794998819088f76b4cf44c8db6940240c563cf4.patch
# Correctly compile the stdatomic.h in ffmpeg with gcc 4.8
#Patch37:	chromium-64.0.3282.119-ffmpeg-stdatomic.patch
# Nacl can't die soon enough
#Patch39:	chromium-66.0.3359.81-system-clang.patch
# Do not prefix libpng functions
#Patch42:	chromium-60.0.3112.78-no-libpng-prefix.patch
# Do not mangle libjpeg
#Patch43:	chromium-60.0.3112.78-jpeg-nomangle.patch
# Do not mangle zlib
#Patch45:	chromium-60.0.3112.78-no-zlib-mangle.patch
# Apply these changes to work around EPEL7 compiler issues
#Patch46:	chromium-62.0.3202.62-kmaxskip-constexpr.patch
#Patch47:	chromium-60.0.3112.90-vulkan-force-c99.patch
# Fix libavutil include pathing to find arch specific timer.h
# For some reason, this only fails on aarch64. No idea why.
#Patch50:	chromium-60.0.3112.113-libavutil-timer-include-path-fix.patch
# from gentoo
#Patch53:	chromium-61.0.3163.79-gcc-no-opt-safe-math.patch
# Only needed when glibc 2.26.90 or later is used
#Patch57:	chromium-63.0.3289.84-aarch64-glibc-2.26.90.patch
# From gentoo
#Patch62:	chromium-65.0.3325.146-gcc5-r3.patch
# To use round with gcc, you need to #include <cmath>
#Patch65:	chromium-65.0.3325.146-gcc-round-fix.patch
# Include proper headers to invoke memcpy()
#Patch67:	chromium-65.0.3325.146-memcpy-fix.patch
# Work around gcc8 bug in gn
#Patch68:	chromium-64.0.3282.167-gcc8-fabi11.patch
# From Gentoo
#Patch69:	chromium-math.h-r0.patch
#Patch70:	chromium-stdint.patch
# Workaround https://gcc.gnu.org/bugzilla/show_bug.cgi?id=80654
# crbug.com/784732#27
# https://chromium-review.googlesource.com/c/chromium/src/+/927942
# https://github.com/lgsvl/meta-lgsvl-browser/blob/ac93e7622be66946c76504be6a1db8d644ae1e43/recipes-browser/chromium/files/0001-GCC-PlaybackImageProvider-Settings-do-not-provide-co.patch
#Patch81:	chromium-65.0.3325.146-GCC-PlaybackImageProvider-Settings-do-not-provide-co.patch
# https://github.com/lgsvl/meta-lgsvl-browser/blob/ac93e7622be66946c76504be6a1db8d644ae1e43/recipes-browser/chromium/files/0001-GCC-explicitely-std-move-to-base-Optional-instead-of.patch
#Patch82:	chromium-65.0.3325.146-GCC-explicitely-std-move-to-base-Optional-instead-of.patch
# https://github.com/lgsvl/meta-lgsvl-browser/blob/ac93e7622be66946c76504be6a1db8d644ae1e43/recipes-browser/chromium/files/0001-GCC-IDB-methods-String-renamed-to-GetString.patch
#Patch83:	chromium-65.0.3325.146-GCC-IDB-methods-String-renamed-to-GetString.patch
# ../../mojo/public/cpp/bindings/associated_interface_ptr_info.h:48:43: error: cannot convert 'const mojo::ScopedInterfaceEndpointHandle' to 'bool' in return
#Patch85:	chromium-67.0.3396.62-boolfix.patch
# From Debian
#Patch86:	chromium-67.0.3396.62-skia-aarch64-buildfix.patch
# Use lstdc++ on EPEL7 only
#Patch87:	chromium-65.0.3325.162-epel7-stdc++.patch
# Clang Gentoo patch: ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-clang-r2.patch
# GCC8 has changed the alignof operator to return the minimal alignment required by the target ABI
# instead of the preferred alignment. This means int64_t is now 4 on i686 (instead of 8).
# Use __alignof__ to get the value we expect (and chromium checks for).
#Patch98:	chromium-66.0.3359.170-gcc8-alignof.patch
# https://chromium.googlesource.com/crashpad/crashpad/+/26ef5c910fc7e2edb441f1d2b39944195342dee9
#Patch99:	chromium-67.0.3396.62-crashpad-aarch64-buildfix.patch
# RHEL 7 has a bug in its python2.7 which does not propely handle exec with a tuple
# https://bugs.python.org/issue21591
#Patch100:	chromium-67.0.3396.62-epel7-use-old-python-exec-syntax.patch
# Gentoo patch ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-widevine-r2.patch
Patch101:	chromium-widevine-r2.patch
# Add "Fedora" to the user agent string
#Patch102:	chromium-67.0.3396.87-russianfedora-user-agent.patch

Patch500:	chromium-clang-r2.patch
# ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-clang-r4.patch
Patch501:	chromium-clang-r4.patch
# ftp://mirror.yandex.ru/gentoo-portage/www-client/chromium/files/chromium-ffmpeg-clang.patch
Patch502:	chromium-ffmpeg-clang.patch
# fix build under ia32
# https://bazaar.launchpad.net/~chromium-team/chromium-browser/bionic-stable/download/head:/fixffmpegia32build.p-20171124052506-76a1tzvpv53mvxrd-1/fix-ffmpeg-ia32-build.patch
Patch503:	fix-ffmpeg-ia32-build.patch
# Vaapi Patches
# Ubuntu patch for chromium 64
# https://raw.githubusercontent.com/saiarcot895/chromium-ubuntu-build/branch-3282/debian/patches/enable_vaapi_on_linux_2.diff
Patch600:	enable_vaapi_on_linux_2.diff

# Use chromium-latest.py to generate clean tarball from released build tarballs, found here:
# http://build.chromium.org/buildbot/official/
# For Chromium Fedora use chromium-latest.py --stable --ffmpegclean --ffmpegarm
# If you want to include the ffmpeg arm sources append the --ffmpegarm switch
# https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%%{version}.tar.xz
#%if %{freeworld}
Source0:	https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
#%else
#Source0:	chromium-%{version}-clean.tar.xz
#%endif
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
# Unpackaged fonts
#Source14:	https://fontlibrary.org/assets/downloads/gelasio/4d610887ff4d445cbc639aae7828d139/gelasio.zip
#Source15:	http://download.savannah.nongnu.org/releases/freebangfont/MuktiNarrow-0.94.tar.bz2

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
BuildRequires:	gtk2-devel
BuildRequires:	glibc-devel
BuildRequires:	gperf
BuildRequires:	libatomic
BuildRequires:	libcap-devel
%if 0%{?bundlelibdrm}
#nothing
%else
BuildRequires:	libdrm-devel
%endif
BuildRequires:	libgcrypt-devel
BuildRequires:	libudev-devel
BuildRequires:	libusb-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXScrnSaver-devel
BuildRequires:	libXtst-devel
BuildRequires:	minizip-devel
BuildRequires:	nodejs
BuildRequires:	nss-devel >= 3.26
BuildRequires:	pciutils-devel
BuildRequires:	pulseaudio-libs-devel
%if 0%{vaapi}
BuildRequires:	libva-devel
%endif

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
%if 0%{?bundlefreetype}
# nothing
%else
BuildRequires:  freetype-devel
%endif
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
%if 0%{?bundlelibjpeg}
# If this is true, we're using the bundled libjpeg
# which we need to do because the RHEL 7 libjpeg doesn't work for chromium anymore
%else
BuildRequires:	libjpeg-devel
%endif
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
BuildRequires:	mesa-libGL-devel
%if %{bundleopus}
# Do nothing
%else
BuildRequires:	opus-devel
%endif
BuildRequires:	perl(Switch)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	python2-devel
%if 0%{?fedora} > 27
BuildRequires:	python2-beautifulsoup4
BuildRequires:	python2-beautifulsoup
BuildRequires:	python2-html5lib
BuildRequires:	python2-markupsafe
BuildRequires:	python2-ply
%else
BuildRequires:	python-beautifulsoup4
BuildRequires:	python-BeautifulSoup
BuildRequires:	python-html5lib
BuildRequires:	python-markupsafe
BuildRequires:	python-ply
%endif
BuildRequires:	python2-simplejson
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
#%if 0%{?rhel} == 7
#Source100:      https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Bold.ttf
#Source101:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-BoldItalic.ttf
#Source102:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Italic.ttf
#Source103:	https://github.com/google/fonts/blob/master/apache/arimo/Arimo-Regular.ttf
#Source104:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Bold.ttf
#Source105:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-BoldItalic.ttf
#Source106:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Italic.ttf
#Source107:	https://github.com/google/fonts/blob/master/apache/cousine/Cousine-Regular.ttf
#Source108:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Bold.ttf
#Source109:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-BoldItalic.ttf
#Source110:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Italic.ttf
#Source111:	https://github.com/google/fonts/blob/master/apache/tinos/Tinos-Regular.ttf
#Source112:	https://releases.pagure.org/lohit/lohit-gurmukhi-ttf-2.91.2.tar.gz
#Source113:	https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKjp-hinted.zip
#%else
#BuildRequires:	google-croscore-arimo-fonts
#BuildRequires:	google-croscore-cousine-fonts
#BuildRequires:  google-croscore-tinos-fonts
#BuildRequires:  google-noto-sans-cjk-jp-fonts
#BuildRequires:  lohit-gurmukhi-fonts
#%endif
#BuildRequires:	dejavu-sans-fonts
#BuildRequires:	thai-scalable-garuda-fonts
#BuildRequires:	lohit-devanagari-fonts
#BuildRequires:	lohit-tamil-fonts
#BuildRequires:	google-noto-sans-khmer-fonts
# using the built from source version on aarch64
BuildRequires:	ninja-build

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

### Chromium Fedora Patches ###
%patch0 -p1 -b .gcc5
#%patch1 -p1 -b .pathmax
#%patch2 -p1 -b .addrfix
#%patch4 -p1 -b .notest
# %%patch6 -p1 -b .gnu-inline
#%patch7 -p1 -b .ignore-fd-count
#%patch9 -p1 -b .modern-libusbx
#%patch12 -p1 -b .cups22
#%patch15 -p1 -b .sandboxpie
#%patch18 -p1 -b .etc
# %%patch19 -p1 -b .madv_free
#%patch20 -p1 -b .gnsystem
%patch21 -p1 -b .lastcommit
#%patch22 -p1 -b .timefix
%patch24 -p1 -b .nullfix
#%patch25 -p1 -b .jpegfix
%patch26 -p1 -b .ldmemory
%patch27 -p1 -b .setopaque
###%patch31 -p1 -b .permissive
###%patch33 -p1 -b .gcc7
%patch36 -p1 -b .revert
#%patch37 -p1 -b .ffmpeg-stdatomic
#%patch39 -p1 -b .system-clang
#%patch42 -p1 -b .noprefix
#%patch43 -p1 -b .nomangle
#%patch45 -p1 -b .nozmangle
#%if 0%{?rhel} == 7
#%patch46 -p1 -b .kmaxskip
# %%patch47 -p1 -b .c99
#%endif
#%patch50 -p1 -b .pathfix
#%patch53 -p1 -b .nogccoptmath
# %%if 0%%{?fedora} >= 28
# %%patch57 -p1 -b .aarch64glibc
# %%endif
#%patch62 -p1 -b .gcc5-r3
###%patch63 -p1 -b .nolibc++
#%patch65 -p1 -b .gcc-round-fix
#%patch67 -p1 -b .memcpyfix
#%if ! 0%{?asan}
#%patch68 -p1 -b .fabi11
#%endif
#%patch81 -p1 -b .pipcc
#%patch82 -p1 -b .explicit-std-move
####%patch83 -p1 -b .GetString
#%patch85 -p1 -b .boolfix
#%patch86 -p1 -b .aarch64fix
#%if 0%{?rhel} == 7
#%patch87 -p1 -b .epel7
#%endif
#%patch98 -p1 -b .gcc8-alignof
#%patch99 -p1 -b .crashpad-aarch64-fix
#%if 0%{?rhel} == 7
#%patch100 -p1 -b .oldexec
#%endif
%patch101 -p1 -b .widevine
#%patch102 -p1 -b .fedora-user-agent
%if 0%{?asan}
%patch500 -p1 -b .clang-r2
%patch501 -p1 -b .clang-r4
%patch502 -p1 -b .clang-ffmpeg
%endif
%ifarch i686
%if 0%{?fedora} >= 28
%patch503 -p1 -b .ia32-ffmpeg
%endif
%endif
%if 0%{vaapi}
%patch600 -p1 -b .vaapi
%endif

# Change shebang in all relevant files in this directory and all subdirectories
# See `man find` for how the `-exec command {} +` syntax works
find -type f -exec sed -i '1s=^#!/usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +

%if 0%{?asan}
export CC="clang"
export CXX="clang++"
%else
export CC="gcc"
export CXX="g++"
%endif
export AR="ar"
export RANLIB="ranlib"

rm -rf buildtools/third_party/libc++/BUILD.gn

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

# Unpack fonts
#pushd third_party/test_fonts
#mkdir test_fonts
#cd test_fonts
#unzip %{SOURCE14}
#tar xf %{SOURCE15}
#mv MuktiNarrow0.94/MuktiNarrow.ttf .
#rm -rf MuktiNarrow0.94
#%if 0%{?rhel} == 7
#cp %{SOURCE100} .
#cp %{SOURCE101} .
#cp %{SOURCE102} .
#cp %{SOURCE103} .
#cp %{SOURCE104} .
#cp %{SOURCE105} .
#cp %{SOURCE106} .
#cp %{SOURCE107} .
#cp %{SOURCE108} .
#cp %{SOURCE109} .
#cp %{SOURCE110} .
#cp %{SOURCE111} .
#tar xf %{SOURCE112}
#mv lohit-gurmukhi-ttf-2.91.2/Lohit-Gurmukhi.ttf .
#rm -rf lohit-gurmukhi-ttf-2.91.2
#unzip %{SOURCE113}
#%else
#cp -a /usr/share/fonts/google-croscore/Arimo-*.ttf .
#cp -a /usr/share/fonts/google-croscore/Cousine-*.ttf .
#cp -a /usr/share/fonts/google-croscore/Tinos-*.ttf .
#cp -a /usr/share/fonts/lohit-gurmukhi/Lohit-Gurmukhi.ttf .
#cp -a /usr/share/fonts/google-noto-cjk/NotoSansCJKjp-Regular.otf .
#%endif
#cp -a /usr/share/fonts/dejavu/DejaVuSans.ttf /usr/share/fonts/dejavu/DejaVuSans-Bold.ttf .
#cp -a /usr/share/fonts/thai-scalable/Garuda.ttf .
#cp -a /usr/share/fonts/lohit-devanagari/Lohit-Devanagari.ttf /usr/share/fonts/lohit-tamil/Lohit-Tamil.ttf .
#cp -a /usr/share/fonts/google-noto/NotoSansKhmer-Regular.ttf .
#popd

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
%if 0%{vaapi}
CHROMIUM_CORE_GN_DEFINES+=' use_vaapi=true'
%endif
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
CHROMIUM_BROWSER_GN_DEFINES+=' use_aura=true'
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
CHROMIUM_HEADLESS_GN_DEFINES+=' enable_nacl=false enable_print_preview=false enable_remoting=false use_alsa=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_cups=false use_dbus=false use_gio=false use_kerberos=false use_libpci=false'
CHROMIUM_HEADLESS_GN_DEFINES+=' use_pulseaudio=false use_udev=false'
export CHROMIUM_HEADLESS_GN_DEFINES

# Remove most of the bundled libraries. Libraries specified below (taken from
# Gentoo's Chromium ebuild) are the libraries that needs to be preserved.
build/linux/unbundle/remove_bundled_libraries.py \
	'buildtools/third_party/libc++' \
	'buildtools/third_party/libc++abi' \
	'base/third_party/dmg_fp' \
	'base/third_party/dynamic_annotations' \
	'base/third_party/icu' \
	'base/third_party/libevent' \
	'base/third_party/nspr' \
	'base/third_party/superfasthash' \
	'base/third_party/symbolize' \
	'base/third_party/valgrind' \
	'base/third_party/xdg_mime' \
	'base/third_party/xdg_user_dirs' \
	'chrome/third_party/mozilla_security_manager' \
	'courgette/third_party' \
	'net/third_party/mozilla_security_manager' \
	'net/third_party/nss' \
	'third_party/WebKit' \
	'third_party/adobe' \
	'third_party/analytics' \
	'third_party/angle' \
	'third_party/angle/src/common/third_party/base' \
	'third_party/angle/src/common/third_party/smhasher' \
	'third_party/angle/src/third_party/compiler' \
	'third_party/angle/src/third_party/libXNVCtrl' \
	'third_party/angle/src/third_party/trace_event' \
	'third_party/angle/third_party/vulkan-validation-layers' \
	'third_party/angle/third_party/glslang' \
	'third_party/angle/third_party/spirv-headers'\
	'third_party/angle/third_party/spirv-tools' \
	'third_party/blanketjs' \
	'third_party/apple_apsl' \
	'third_party/blink' \
	'third_party/boringssl' \
	'third_party/boringssl/src/third_party/fiat' \
	'third_party/breakpad' \
	'third_party/breakpad/breakpad/src/third_party/curl' \
	'third_party/brotli' \
	'third_party/cacheinvalidation' \
	'third_party/catapult' \
	'third_party/catapult/common/py_vulcanize/third_party/rcssmin' \
	'third_party/catapult/common/py_vulcanize/third_party/rjsmin' \
	'third_party/catapult/third_party/polymer' \
	'third_party/catapult/tracing/third_party/d3' \
	'third_party/catapult/tracing/third_party/gl-matrix' \
	'third_party/catapult/tracing/third_party/jszip' \
	'third_party/catapult/tracing/third_party/mannwhitneyu' \
	'third_party/catapult/tracing/third_party/oboe' \
	'third_party/catapult/tracing/third_party/pako' \
        'third_party/ced' \
	'third_party/cld_3' \
	'third_party/crashpad' \
	'third_party/crashpad/crashpad/third_party/zlib' \
	'third_party/crc32c' \
	'third_party/cros_system_api' \
	'third_party/devscripts' \
	'third_party/dom_distiller_js' \
	'third_party/expat' \
	'third_party/ffmpeg' \
	'third_party/fips181' \
	'third_party/flac' \
        'third_party/flatbuffers' \
	'third_party/flot' \
	'third_party/fontconfig' \
	'third_party/freetype' \
	'third_party/glslang-angle' \
	'third_party/google_input_tools' \
	'third_party/google_input_tools/third_party/closure_library' \
	'third_party/google_input_tools/third_party/closure_library/third_party/closure' \
	'third_party/googletest' \
	'third_party/harfbuzz-ng' \
	'third_party/hunspell' \
	'third_party/iccjpeg' \
	'third_party/icu' \
	'third_party/inspector_protocol' \
	'third_party/jinja2' \
	'third_party/jstemplate' \
	'third_party/khronos' \
	'third_party/leveldatabase' \
	'third_party/libXNVCtrl' \
	'third_party/libaddressinput' \
	'third_party/libaom' \
	'third_party/libaom/source/libaom/third_party/x86inc' \
	'third_party/libdrm' \
	'third_party/libjingle' \
	'third_party/libjpeg_turbo' \
	'third_party/libphonenumber' \
	'third_party/libpng' \
	'third_party/libsecret' \
        'third_party/libsrtp' \
	'third_party/libudev' \
	'third_party/libusb' \
	'third_party/libvpx' \
	'third_party/libvpx/source/libvpx/third_party/x86inc' \
	'third_party/libxml' \
	'third_party/libxml/chromium' \
	'third_party/libxslt' \
	'third_party/libwebm' \
	'third_party/libwebp' \
	'third_party/libyuv' \
%if 0%{?nacl}
	'third_party/llvm-build' \
%endif
	'third_party/lss' \
	'third_party/lzma_sdk' \
%if 0
	'third_party/markupsafe' \
%endif
	'third_party/mesa' \
	'third_party/metrics_proto' \
	'third_party/modp_b64' \
	'third_party/node' \
	'third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2' \
%if %{freeworld}
	'third_party/openh264' \
%endif
	'third_party/openmax_dl' \
	'third_party/opus' \
	'third_party/ots' \
	'third_party/pdfium' \
	'third_party/pdfium/third_party/agg23' \
	'third_party/pdfium/third_party/base' \
	'third_party/pdfium/third_party/bigint' \
	'third_party/pdfium/third_party/freetype' \
	'third_party/pdfium/third_party/lcms' \
	'third_party/pdfium/third_party/libopenjpeg20' \
        'third_party/pdfium/third_party/libpng16' \
        'third_party/pdfium/third_party/libtiff' \
        'third_party/pdfium/third_party/skia_shared' \
        'third_party/ply' \
	'third_party/polymer' \
	'third_party/protobuf' \
	'third_party/protobuf/third_party/six' \
	'third_party/qcms' \
	'third_party/qunit' \
%if 0%{?bundlere2}
	'third_party/re2' \
%endif
	'third_party/s2cellid' \
	'third_party/sfntly' \
	'third_party/sinonjs' \
	'third_party/skia' \
	'third_party/skia/third_party/gif' \
	'third_party/skia/third_party/vulkan' \
	'third_party/smhasher' \
	'third_party/snappy' \
	'third_party/speech-dispatcher' \
	'third_party/spirv-headers' \
	'third_party/spirv-tools-angle' \
	'third_party/sqlite' \
	'third_party/swiftshader' \
	'third_party/swiftshader/third_party/subzero' \
	'third_party/swiftshader/third_party/LLVM' \
	'third_party/swiftshader/third_party/llvm-subzero' \
	'third_party/test_fonts' \
	'third_party/tcmalloc' \
	'third_party/unrar' \
        'third_party/usb_ids' \
	'third_party/usrsctp' \
	'third_party/vulkan' \
	'third_party/vulkan-validation-layers' \
	'third_party/web-animations-js' \
	'third_party/webdriver' \
	'third_party/webrtc' \
	'third_party/widevine' \
        'third_party/woff2' \
        'third_party/xdg-utils' \
        'third_party/yasm' \
        'third_party/zlib' \
	'third_party/zlib/google' \
	'url/third_party/mozilla' \
	'v8/src/third_party/utf8-decoder' \
	'v8/src/third_party/valgrind' \
	'v8/third_party/inspector_protocol' \
	--do-remove

# Look, I don't know. This package is spit and chewing gum. Sorry.
rm -rf third_party/markupsafe
ln -s %{python2_sitearch}/markupsafe third_party/markupsafe
# We should look on removing other python2 packages as well i.e. ply

%if %{build_remote_desktop}
# Fix hardcoded path in remoting code
sed -i 's|/opt/google/chrome-remote-desktop|%{crd_path}|g' remoting/host/setup/daemon_controller_delegate_linux.cc
%endif

export PATH=$PATH:%{_builddir}/depot_tools

build/linux/unbundle/replace_gn_files.py --system-libraries \
	flac \
%if 0%{?bundlefontconfig}
%else
	fontconfig \
%endif
%if 0%{?bundlefreetype}
%else
	freetype \
%endif
%if 0%{?bundleharfbuzz}
%else
	harfbuzz-ng \
%endif
%if 0%{?bundleicu}
%else
	icu \
%endif
%if %{bundlelibdrm}
%else
	libdrm \
%endif
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

# fix arm gcc
sed -i 's|arm-linux-gnueabihf-|arm-linux-gnu-|g' build/toolchain/linux/BUILD.gn

%ifarch aarch64
# We don't need to cross compile while building on an aarch64 system.
sed -i 's|aarch64-linux-gnu-||g' build/toolchain/linux/BUILD.gn

# Correct the ninja file to check for aarch64, not just x86.
sed -i '/${LONG_BIT}/ a \      aarch64)\' ../depot_tools/ninja
sed -i '/aarch64)/ a \        exec "/usr/bin/ninja-build" "$@";;\' ../depot_tools/ninja
%endif

%if 0%{?rhel} == 7
sed -i "s@'ninja'@'ninja-build'@g" tools/gn/bootstrap/bootstrap.py
. /opt/rh/devtoolset-7/enable
%endif

# Check that there is no system 'google' module, shadowing bundled ones:
if python2 -c 'import google ; print google.__path__' 2> /dev/null ; then \
    echo "Python 2 'google' module is defined, this will shadow modules of this build"; \
    exit 1 ; \
fi

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

# setup node
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s /usr/bin/node third_party/node/linux/node-linux-x64/bin/node

%build
%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
NINJA="ninja-build"
%else
NINJA="ninja"
%endif

# Now do the full browser
# Do headless first.
#$NINJA -C %{headlesstarget} -vvv headless_shell

sed -i 's@gn @./gn @g' out/Release/build.ninja

$NINJA -C %{target} -vvv libffmpeg.so

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
* Thu Jun 28 2018 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:67.0.3396.87-1
- Update to 67.0.3396.87
- Match Opera version 54.0.2952.41
- Sync *.spec file to Arkady L. Shane's chromium.spec (version: 67.0.3396.87-2)

* Wed Apr 25 2018 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:65.0.3325.181-1
- Update to 65.0.3325.181
- Match Opera version 52.0.2871.97
- Sync *.spec file to Arkady L. Shane's chromium.spec (version: 65.0.3325.181-1)

* Mon Feb 19 2018 carasin berlogue <carasin DOT berlogue AT mail DOT ru> - 5:64.0.3282.140-1
- Update to 64.0.3282.140
- Match Opera version 51.0.2830.34

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
