#Global Libraries
#Do not turn it on in Fedora copr!
%global freeworld 1
#This can be any folder on out
%global target out/Release
%global orig_name chromium-freeworld
### Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
### Note: These are for Fedora use ONLY.
### For your own distribution, please get your own set of keys.
### http://lists.debian.org/debian-legal/2013/11/msg00006.html
%global api_key AIzaSyDUIXvzVrt5OkVsgXhQ6NFfvWlA44by-aw
%global default_client_id 449907151817.apps.googleusercontent.com
%global default_client_secret miEreAep8nuvTdvLums6qyLK
###############################Exclude Private chromium libs###########################
%global __requires_exclude %{chromiumdir}/.*\\.so
%global __provides_exclude_from %{chromiumdir}/.*\\.so
#######################################CONFIGS###########################################
# Fedora's Python 2 stack is being removed, we use the bundled Python libraries
# This can be revisited once we upgrade to Python 3
%global bundlepylibs 1
%if 0%{bundlepylibs}
%bcond_with system_ply
%else
%bcond_without system_ply
%endif
# This package depends on automagic byte compilation
# https://fedoraproject.org/wiki/Changes/No_more_automagic_Python_bytecompilation_phase_2
%global _python_bytecompile_extra 1
#Require harfbuzz >= 2.4.0 for hb_subset_input_set_retain_gids
%if 0%{?fedora} >= 31
%bcond_without system_harfbuzz
%else
%bcond_with system_harfbuzz
%endif
# Require libxml2 > 2.9.4 for XML_PARSE_NOXXE
%bcond_without system_libxml2

# Clang toggle
%global clang 0

# Allow testing whether icu can be unbundled
# A patch fix building so enabled by default for Fedora 30
# Need icu version >= 64
%bcond_with system_libicu
%if 0%{?fedora} >= 31
# Allow testing whether libvpx can be unbundled
%bcond_with system_libvpx
# Allow testing whether ffmpeg can be unbundled
%bcond_with system_ffmpeg
#Allow minizip to be unbundled
#mini-compat is going to be removed from fedora 30!
%bcond_without system_minizip
%else
%bcond_with system_libvpx
%bcond_with system_ffmpeg
#Allow minizip to be unbundled
#mini-compat is going to be removed from fedora 30!
%bcond_without system_minizip
%endif

# Need re2 ver. 2016.07.21 for re2::LazyRE2
%bcond_with system_re2

#Turn on verbose mode
%global debug_logs 0
#------------------------------------------------------
#Build debug packages for debugging
%global debug_pkg 0
# Enable building with ozone support
%global ozone 0
##############################Package Definitions######################################
Name:           opera-libffmpeg
Version:        81.0.4044.92
Release:        1%{?dist}
Summary:        Additional FFmpeg library for Opera Web browser providing H264 and MP4 support
License:        BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)
URL:            https://gist.github.com/lukaszzek/ec04d5c953226c062dac
%if %{freeworld}
Source0:        https://commondatastorage.googleapis.com/chromium-browser-official/chromium-%{version}.tar.xz
%else
# Unfortunately, Fedora & Copr forbids uploading sources with patent-encumbered
# ffmpeg code even if they are never compiled and linked to target binaries,
# so we must repackage upstream tarballs to satisfy this requirement. However,
# we cannot simply delete all code of ffmpeg because this will disable support
# for some commonly-used free codecs such as Ogg Theora. Instead, helper
# scripts included in official Fedora packages are copied, modified, and used
# to automate the repackaging work.
# Get those helper scripts from https://src.fedoraproject.org/rpms/chromium
# If you don't use Fedora services, Just set the value of freeworld in this spec file
# to 1 to use the upstreanm packaged source.
# The repackaged source tarball used here is produced by:
# ./chromium-latest.py --stable --ffmpegclean --ffmpegarm --deleteunrar
Source0:        chromium-%{version}-clean.tar.xz
%endif
# The following two source files are copied and modified from the chromium source
#Source10:       %{orig_name}.sh
#Add our own appdata file.
#Source11:       %{orig_name}.appdata.xml
#Personal stuff
Source15:       LICENSE
######################## Installation Folder #################################################
#Our installation folder
%global chromiumdir %{_libdir}/%{orig_name}
########################################################################################
#Compiler settings
# Make sure we don't encounter any bug
%if %{clang}
BuildRequires:  clang, llvm, lld
%else
BuildRequires:  gcc-c++
%endif
# Basic tools and libraries needed for building
BuildRequires:  ninja-build, nodejs, bison, gperf, hwdata
BuildRequires:  libgcc, glibc, libatomic
BuildRequires:  libcap-devel, cups-devel, alsa-lib-devel
BuildRequires:  mesa-libGL-devel, mesa-libEGL-devel
%if %{with system_minizip}
BuildRequires:  minizip-compat-devel
%endif
# Pipewire need this.
%if 0%{?fedora} >= 29
BuildRequires:  pkgconfig(libpipewire-0.2)
%endif
BuildRequires:  pkgconfig(gtk+-2.0), pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libexif), pkgconfig(nss)
BuildRequires:  pkgconfig(xtst), pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(dbus-1), pkgconfig(libudev)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(libffi)
#for vaapi
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(gbm)
%if %{ozone}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
%endif

#Python stuffs
%if 0%{?bundlepylibs}

# Using bundled bits, do nothing.
#This is needed for remove_bundled_libraries.py
BuildRequires:  /usr/bin/python2

%else
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-beautifulsoup4
BuildRequires:  python2-lxml
BuildRequires:  python2-html5lib
BuildRequires:  python2-markupsafe
Buildrequires:  python2-six
%if %{with system_ply}
BuildRequires:  python2-ply
%endif
%endif
%if %{with system_re2}
BuildRequires:  re2-devel
%endif
# replace_gn_files.py --system-libraries
BuildRequires:  flac-devel
BuildRequires:  freetype-devel
%if %{with system_harfbuzz}
BuildRequires:  harfbuzz-devel
%endif
%if %{with system_libicu}
BuildRequires:  libicu-devel
%endif
BuildRequires:  libdrm-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libpng-devel
# Chromium requires libvpx 1.5.0 and some non-default options
%if %{with system_libvpx}
BuildRequires:  libvpx-devel
%endif
%if %{with system_ffmpeg}
BuildRequires:  ffmpeg-devel
%endif
BuildRequires:  libwebp-devel
%if %{with system_libxml2}
BuildRequires:  pkgconfig(libxml-2.0)
%endif
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  opus-devel
BuildRequires:  snappy-devel
BuildRequires:  yasm
BuildRequires:  expat-devel
BuildRequires:  pciutils-devel
BuildRequires:  speech-dispatcher-devel
BuildRequires:  pulseaudio-libs-devel
# install desktop files
BuildRequires:  desktop-file-utils
# install AppData files
BuildRequires:  libappstream-glib
# Mojojojo need this >:(
BuildRequires:  java-1.8.0-openjdk
# Libstdc++ static needed for linker
BuildRequires:  libstdc++-static
%if !%{debug_pkg}
%global debug_package %{nil}
%endif
# This build should be only available to amd64
ExclusiveArch:  x86_64

# Google patches (short-term fixes and backports):
Patch150:       chromium-81-vaapi-r737459.patch
Patch151:       chromium-81-vaapi-r738595.patch
Patch152:       chromium-81-gcc-r742632.patch
Patch153:       chromium-81-gcc-r742834.patch
Patch154:       chromium-81-gcc-r743910.patch

# Gentoo patches (short-term fixes):
%if 0%{?fedora} >= 32
Patch250:       chromium-81-gcc-10.patch
%endif

# Fedora patches:
Patch300:       chromium-71.0.3578.98-py2-bootstrap.patch

# RPM Fusion patches [free/chromium-freeworld]:
Patch400:       chromium-enable-vaapi.patch
Patch401:       chromium-fix-vaapi-on-intel.patch
Patch402:       chromium-enable-widevine.patch
%if %{freeworld}
Patch403:       chromium-rpm-fusion-brand.patch
%endif

%description
Due to changes in Chromium, Opera is no longer able to use the system FFmpeg
library for H264 video playback on Linux, so H264-encoded videos fail to play by
default (but HTML5 video encoded using different formats, like webm, work). For
legal reasons, Opera may not be distributed with H264 compatible FFmpeg library
included into package.

It's possible to build the extra version of Chromium modified FFmpeg providing
H264 and MP4 support. Opera-libffmpeg package includes this library.
############################################PREP###########################################################
%prep
%autosetup -n chromium-%{version} -p1

#Let's change the default shebang of python files.
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python2}=' {} +
./build/linux/unbundle/remove_bundled_libraries.py --do-remove \
    base/third_party/cityhash \
    base/third_party/double_conversion \
    base/third_party/dynamic_annotations \
    base/third_party/icu \
    base/third_party/libevent \
    base/third_party/nspr \
    base/third_party/superfasthash \
    base/third_party/symbolize \
    base/third_party/valgrind \
    base/third_party/xdg_mime \
    base/third_party/xdg_user_dirs \
    buildtools/third_party/libc++ \
    buildtools/third_party/libc++abi \
    chrome/third_party/mozilla_security_manager \
    courgette/third_party \
    native_client/src/third_party/dlmalloc \
    native_client/src/third_party/valgrind \
    net/third_party/mozilla_security_manager \
    net/third_party/nss \
    net/third_party/quic \
    net/third_party/uri_template \
    third_party/abseil-cpp \
    third_party/adobe \
    third_party/angle \
    third_party/angle/src/common/third_party/base \
    third_party/angle/src/common/third_party/smhasher \
    third_party/angle/src/common/third_party/xxhash \
    third_party/angle/src/third_party/compiler \
    third_party/angle/src/third_party/libXNVCtrl \
    third_party/angle/src/third_party/trace_event \
    third_party/angle/src/third_party/volk \
    third_party/libgifcodec \
    third_party/glslang \
    third_party/angle/third_party/spirv-headers \
    third_party/angle/third_party/spirv-tools \
    third_party/angle/third_party/vulkan-headers \
    third_party/angle/third_party/vulkan-loader \
    third_party/angle/third_party/vulkan-tools \
    third_party/angle/third_party/vulkan-validation-layers \
    third_party/apple_apsl \
    third_party/axe-core \
    third_party/boringssl \
    third_party/boringssl/src/third_party/fiat \
    third_party/blink \
    third_party/breakpad \
    third_party/breakpad/breakpad/src/third_party/curl \
    third_party/brotli \
    third_party/cacheinvalidation \
    third_party/catapult \
    third_party/catapult/common/py_vulcanize/third_party/rcssmin \
    third_party/catapult/common/py_vulcanize/third_party/rjsmin \
%if 0%{?bundlepylibs}
    third_party/catapult/third_party/beautifulsoup4 \
    third_party/catapult/third_party/html5lib-python \
%endif
    third_party/catapult/third_party/polymer \
    third_party/catapult/third_party/six \
    third_party/catapult/tracing/third_party/d3 \
    third_party/catapult/tracing/third_party/gl-matrix \
    third_party/catapult/tracing/third_party/jpeg-js \
    third_party/catapult/tracing/third_party/jszip \
    third_party/catapult/tracing/third_party/mannwhitneyu \
    third_party/catapult/tracing/third_party/oboe \
    third_party/catapult/tracing/third_party/pako \
    third_party/ced \
    third_party/cld_3 \
    third_party/closure_compiler \
    third_party/crashpad \
    third_party/crashpad/crashpad/third_party/lss \
    third_party/crashpad/crashpad/third_party/zlib \
    third_party/crc32c \
    third_party/cros_system_api \
    third_party/dawn \
    third_party/depot_tools \
    third_party/dav1d \
    third_party/devscripts \
    third_party/devtools-frontend \
    third_party/devtools-frontend/src/front_end/third_party/fabricjs \
    third_party/devtools-frontend/src/front_end/third_party/wasmparser \
    third_party/devtools-frontend/src/third_party \
    third_party/dom_distiller_js \
    third_party/emoji-segmenter \
%if !%{with system_ffmpeg}
    third_party/ffmpeg \
%endif
    third_party/flatbuffers \
    third_party/freetype \
    third_party/google_input_tools \
    third_party/google_input_tools/third_party/closure_library \
    third_party/google_input_tools/third_party/closure_library/third_party/closure \
    third_party/googletest \
%if !%{with system_harfbuzz}
    third_party/harfbuzz-ng \
%endif
    third_party/hunspell \
    third_party/iccjpeg \
%if !%{with system_libicu}
    third_party/icu \
%endif
    third_party/inspector_protocol \
    third_party/jinja2 \
    third_party/jsoncpp \
    third_party/jstemplate \
    third_party/khronos \
    third_party/leveldatabase \
    third_party/libaddressinput \
    third_party/libaom \
    third_party/libaom/source/libaom/third_party/vector \
    third_party/libaom/source/libaom/third_party/x86inc \
    third_party/libjingle \
    third_party/libphonenumber \
    third_party/libsecret \
    third_party/libsrtp \
    third_party/libsync \
    third_party/libudev \
%if !%{with system_libvpx}
    third_party/libvpx \
    third_party/libvpx/source/libvpx/third_party/x86inc \
%endif
    third_party/libwebm \
%if %{with system_libxml2}
    third_party/libxml/chromium \
%else
    third_party/libxml \
%endif
    third_party/libXNVCtrl \
    third_party/libyuv \
    third_party/lss \
    third_party/lzma_sdk \
%if 0%{?bundlepylibs}
    third_party/markupsafe \
%endif
    third_party/mesa \
    third_party/metrics_proto \
%if %{ozone}
    third_party/minigbm \
%endif
%if !%{with system_minizip}
    third_party/minizip/ \
%endif
    third_party/modp_b64 \
    third_party/nasm \
    third_party/node \
    third_party/node/node_modules/polymer-bundler/lib/third_party/UglifyJS2 \
    third_party/one_euro_filter \
    third_party/openh264 \
    third_party/openscreen \
    third_party/openscreen/src/third_party/tinycbor/src/src \
    third_party/ots \
    third_party/pdfium \
    third_party/pdfium/third_party/agg23 \
    third_party/pdfium/third_party/base \
    third_party/pdfium/third_party/bigint \
    third_party/pdfium/third_party/freetype \
    third_party/pdfium/third_party/lcms \
    third_party/pdfium/third_party/libopenjpeg20 \
    third_party/pdfium/third_party/libpng16 \
    third_party/pdfium/third_party/libtiff \
    third_party/pdfium/third_party/skia_shared \
    third_party/perfetto \
    third_party/pffft \
%if !%{with system_ply}
    third_party/ply \
%endif
    third_party/polymer \
    third_party/private-join-and-compute \
    third_party/protobuf \
    third_party/protobuf/third_party/six \
    third_party/pyjson5 \
    third_party/qcms \
%if !%{with system_re2}
    third_party/re2 \
%endif
    third_party/rnnoise \
    third_party/s2cellid \
    third_party/skia \
    third_party/skia/include/third_party/skcms \
    third_party/skia/include/third_party/vulkan \
    third_party/skia/third_party/vulkan \
    third_party/skia/third_party/skcms \
    third_party/smhasher \
    third_party/speech-dispatcher \
    third_party/spirv-headers \
    third_party/SPIRV-Tools \
    third_party/sqlite \
    third_party/swiftshader \
    third_party/swiftshader/third_party/llvm-7.0 \
    third_party/swiftshader/third_party/llvm-subzero \
    third_party/swiftshader/third_party/marl \
    third_party/swiftshader/third_party/subzero \
    third_party/swiftshader/third_party/SPIRV-Headers/include/spirv/unified1 \
    third_party/tcmalloc \
    third_party/unrar \
    third_party/usb_ids \
    third_party/usrsctp \
    third_party/vulkan \
%if %{ozone}
    third_party/wayland \
%endif
    third_party/web-animations-js \
    third_party/webdriver \
    third_party/webrtc \
    third_party/webrtc/common_audio/third_party/fft4g \
    third_party/webrtc/common_audio/third_party/spl_sqrt_floor \
    third_party/webrtc/modules/third_party/fft \
    third_party/webrtc/modules/third_party/g711 \
    third_party/webrtc/modules/third_party/g722 \
    third_party/webrtc/rtc_base/third_party/base64 \
    third_party/webrtc/rtc_base/third_party/sigslot \
    third_party/widevine \
    third_party/woff2 \
    third_party/xdg-utils \
    third_party/yasm/run_yasm.py \
    third_party/zlib/google \
    tools/grit/third_party/six \
%if !%{with system_minizip}
    third_party/zlib \
%endif
    tools/gn/src/base/third_party/icu \
    url/third_party/mozilla \
    v8/src/third_party/siphash \
    v8/src/third_party/valgrind \
    v8/src/third_party/utf8-decoder \
    v8/third_party/inspector_protocol \
    v8/third_party/v8

./build/linux/unbundle/replace_gn_files.py --system-libraries \
%if %{with system_ffmpeg}
    ffmpeg \
%endif
    flac \
    freetype \
    fontconfig \
%if %{with system_libicu}
    icu \
%endif
    libdrm \
    libjpeg \
    libpng \
%if %{with system_libvpx}
    libvpx \
%endif
    libwebp \
%if %{with system_libxml2}
    libxml \
%endif
    libxslt \
    opus \
%if %{with system_re2}
    re2 \
%endif
    snappy \
    yasm \
%if %{with system_minizip}
    zlib
%endif

sed -i 's|//third_party/usb_ids|/usr/share/hwdata|g' \
    services/device/public/cpp/usb/BUILD.gn

%if !0%{?bundlepylibs}
rmdir third_party/markupsafe
ln -s %{python2_sitearch}/markupsafe third_party/markupsafe
%if %{with system_ply}
rmdir third_party/ply
ln -s %{python2_sitelib}/ply third_party/ply
%endif
%endif

# Fix the path to nodejs binary
mkdir -p third_party/node/linux/node-linux-x64/bin
ln -s %{_bindir}/node third_party/node/linux/node-linux-x64/bin/node
#####################################BUILD#############################################
%build
#export compilar variables

%if %{clang}

export AR=llvm-ar NM=llvm-nm AS=llvm-as
export CC=clang CXX=clang++

# Add required compiler flags here
export CXXFLAGS="$CXXFLAGS -Wno-unknown-warning-option"
export CFLAGS="$CFLAGS -Wno-unknown-warning-option"

%else
export AR=ar NM=nm AS=as
export CC=gcc CXX=g++


# GN needs gold to bootstrap
export LDFLAGS="$LDFLAGS -fuse-ld=gold"

export CXXFLAGS="$CXXFLAGS -fpermissive"
%if !%{debug_logs}
# Disable useless warning on non debug log builds
export CFLAGS="$CFLAGS -w"
export CXXFLAGS="$CXXFLAGS -w"
%endif
%if !%{debug_pkg}
export CFLAGS="$CFLAGS -g0"
export CXXFLAGS="$CXXFLAGS -g0"
%endif
%if 0%{?fedora} <= 29
export CXXFLAGS="$CXXFLAGS -fno-ipa-cp-clone"
%endif
#end compiler part
%endif

gn_args=(
    is_debug=false
    use_vaapi=true
    is_component_build=false
    use_sysroot=false
    use_custom_libcxx=false
    use_aura=true
    'system_libdir="%{_lib}"'
    use_cups=true
    use_gnome_keyring=true
    use_gio=true
    use_kerberos=true
    use_libpci=true
    use_pulseaudio=true
    link_pulseaudio=true
    use_system_freetype=true
    enable_widevine=true
%if %{with system_harfbuzz}
    use_system_harfbuzz=true
%endif
%if %{freeworld}
    'ffmpeg_branding="Chrome"'
    proprietary_codecs=true
    enable_platform_hevc=true
    enable_platform_ac3_eac3_audio=true
    enable_platform_mpeg_h_audio=true
    enable_platform_dolby_vision=true
    enable_mse_mpeg2ts_stream_parser=true
    is_component_ffmpeg=true
%else
    'ffmpeg_branding="Chromium"'
    proprietary_codecs=false
%endif
    enable_nacl=false
    enable_hangout_services_extension=false
    fatal_linker_warnings=false
    treat_warnings_as_errors=false
    linux_use_bundled_binutils=false
    fieldtrial_testing_like_official_build=true
    'custom_toolchain="//build/toolchain/linux/unbundle:default"'
    'host_toolchain="//build/toolchain/linux/unbundle:default"'
    'google_api_key="%{api_key}"'
    'google_default_client_id="%{default_client_id}"'
    'google_default_client_secret="%{default_client_secret}"'
)

# Optimizations
gn_args+=(
   enable_vr=false
%if %{with system_libicu}
   icu_use_data_file=false
%endif
)


gn_args+=(
%if %{clang}
    is_clang=true
    'clang_base_path="/usr"'
    clang_use_chrome_plugins=false
    use_lld=true
%else
    is_clang=false
%endif
)

#Pipewire
gn_args+=(
%if 0%{?fedora} >= 29
     rtc_use_pipewire=true
     rtc_link_pipewire=true
%endif
)

# Ozone stuff : Whole work is done completely upstream.
gn_args+=(
%if %{ozone}
    use_ozone=true
    use_system_minigbm=true
    use_xkbcommon=true
%endif
)


#symbol
gn_args+=(
%if %{debug_pkg}
    symbol_level=1
%else
    symbol_level=0
    blink_symbol_level=0
%endif
)
tools/gn/bootstrap/bootstrap.py  --gn-gen-args "${gn_args[*]}"
%{target}/gn --script-executable=%{__python2} gen --args="${gn_args[*]}" %{target}
%if %{debug_logs}
ninja %{_smp_mflags} -C %{target} -v third_party/ffmpeg
%else
ninja %{_smp_mflags} -C %{target} third_party/ffmpeg
%endif
######################################Install####################################
%install
mkdir -p %{buildroot}%{_libdir}/opera/lib_extra
install -m 644 %{target}/libffmpeg.so %{buildroot}%{_libdir}/opera/lib_extra/
####################################check##################################################
#%check
#appstream-util validate-relax --nonet "%{buildroot}%{_metainfodir}/%{orig_name}.appdata.xml"
######################################files################################################
%files
%{_libdir}/opera/lib_extra/libffmpeg.so
#########################################changelogs#################################################
%changelog
* Sun May 03 2020 carasin <carasin.berlogue@mail.ru>
- Create package opera-libffmpeg based on chromium-freeworld

* Thu Apr 09 2020 qvint <dotqvint@gmail.com> - 81.0.4044.92-1
- Update to 81.0.4044.92

* Sun Apr 05 2020 qvint <dotqvint@gmail.com> - 80.0.3987.163-1
- Update to 80.0.3987.163

* Thu Apr 02 2020 qvint <dotqvint@gmail.com> - 80.0.3987.162-1
- Update to 80.0.3987.162

* Wed Mar 18 2020 qvint <dotqvint@gmail.com> - 80.0.3987.149-1
- Update to 80.0.3987.149
- Fix rpmlint warnings and errors

* Wed Mar 04 2020 qvint <dotqvint@gmail.com> - 80.0.3987.132-1
- Update to 80.0.3987.132

* Sun Mar 01 2020 qvint <dotqvint@gmail.com> - 80.0.3987.122-1
- Update to 80.0.3987.122

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 79.0.3945.130-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Vasiliy Glazov <vascom2@gmail.com> - 79.0.3945.130-1
- Update to 79.0.3945.130

* Tue Jan 14 2020 Vasiliy Glazov <vascom2@gmail.com> - 79.0.3945.117-1
- Update to 79.0.3945.117

* Sat Dec 21 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 79.0.3945.88-1
- Update to 79.0.3945.88

* Fri Dec 13 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 79.0.3945.79-1
- Update to 79.0.3945.79

* Fri Dec 06 2019 Vasiliy Glazov <vascom2@gmail.com> - 78.0.3904.108-2
- Disable fedora's build flags to reduce binary size

* Thu Nov 21 2019 Vasiliy Glazov <vascom2@gmail.com> - 78.0.3904.108-1
- Update to 78.0.3904.108

* Tue Nov 12 2019 Vasiliy Glazov <vascom2@gmail.com> - 78.0.3904.97-1
- Update to 78.0.3904.97

* Sat Nov 02 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 78.0.3904.87-1
- Update to 78.0.3904.87

* Thu Oct 31 2019 Akarshan Biswas <akarshanbiswas@fedoraproject.org> - 78.0.3904.70-1
- IMPORT: rename package; add back Fedora build flags
