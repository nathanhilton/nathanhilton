load("@rules_python//python:py_library.bzl", "py_library")
load("@rules_python//python:py_test.bzl", "py_test")
load("@py_deps//:requirements.bzl", "requirement")

py_library(
    name = "request",
    srcs = ["request.py"],
    deps = [requirement("aiohttp")],
)

py_test(
    name = "test_request",
    srcs = ["test_request.py"],
    deps = [":request"],
)
