load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

############################################################ Python ############################################################
RULES_PYTHON_VERSION="0.26.0"
RULES_PYTHON_SHA="9d04041ac92a0985e344235f5d946f71ac543f1b1565f2cdbc9a2aaee8adf55b"
http_archive(
    name = "rules_python",
    sha256 = RULES_PYTHON_SHA,
    strip_prefix = "rules_python-" + RULES_PYTHON_VERSION,
    url = "https://github.com/bazelbuild/rules_python/releases/download/" + RULES_PYTHON_VERSION + "/rules_python-" + RULES_PYTHON_VERSION + ".tar.gz",
)

load("@rules_python//python:repositories.bzl", "py_repositories")

py_repositories()
 
load("@rules_python//python:repositories.bzl", "python_register_toolchains")

PYTHON_VERSION="3.10"
python_register_toolchains(
    name = "hermetic_python",
    python_version = PYTHON_VERSION,
)
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
