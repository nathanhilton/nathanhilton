load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

######################################################### Bazel-skylib #########################################################

BAZEL_SKYLIB_VERSION="1.5.0"
BAZEL_SKYLIB_SHA="cd55a062e763b9349921f0f5db8c3933288dc8ba4f76dd9416aac68acee3cb94"
http_archive(
    name = "bazel_skylib",
    sha256 = BAZEL_SKYLIB_SHA,
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/bazel-skylib/releases/download/" + BAZEL_SKYLIB_VERSION + "/bazel-skylib-" + BAZEL_SKYLIB_VERSION + ".tar.gz",
        "https://github.com/bazelbuild/bazel-skylib/releases/download/" + BAZEL_SKYLIB_VERSION + "/bazel-skylib-" + BAZEL_SKYLIB_VERSION + ".tar.gz",
    ],
)

load("@bazel_skylib//:workspace.bzl", "bazel_skylib_workspace")

bazel_skylib_workspace()

################################################################################################################################

############################################################ Python ############################################################

RULES_PYTHON_VERSION="0.25.0"
RULES_PYTHON_SHA="5868e73107a8e85d8f323806e60cad7283f34b32163ea6ff1020cf27abef6036"
http_archive(
    name = "rules_python",
    sha256 = RULES_PYTHON_SHA,
    strip_prefix = "rules_python-" + RULES_PYTHON_VERSION,
    url = "https://github.com/bazelbuild/rules_python/releases/download/" + RULES_PYTHON_VERSION + "/rules_python-" + RULES_PYTHON_VERSION + ".tar.gz",
)
 
load("@rules_python//python:repositories.bzl", "python_register_toolchains")

PYTHON_VERSION="3.10"
python_register_toolchains(
    name = "hermetic_python",
    python_version = PYTHON_VERSION,
)

load("@rules_python//python:pip.bzl", "pip_parse")
load("@hermetic_python//:defs.bzl", "interpreter")

pip_parse(
    name = "py_deps",
    python_interpreter_target = interpreter,
    requirements_lock = "//third-party/py/private/generated:requirements.txt",
)

load("@py_deps//:requirements.bzl", "install_deps")

install_deps()

#################################################################################################################################

############################################################## Go ###############################################################

http_archive(
    name = "io_bazel_rules_go",
    sha256 = "91585017debb61982f7054c9688857a2ad1fd823fc3f9cb05048b0025c47d023",
    urls = [
        "https://mirror.bazel.build/github.com/bazelbuild/rules_go/releases/download/v0.42.0/rules_go-v0.42.0.zip",
        "https://github.com/bazelbuild/rules_go/releases/download/v0.42.0/rules_go-v0.42.0.zip",
    ],
)

load("@io_bazel_rules_go//go:deps.bzl", "go_register_toolchains", "go_rules_dependencies")

go_rules_dependencies()

go_register_toolchains(version = "1.21.1")

#################################################################################################################################
