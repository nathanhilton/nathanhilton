load("@rules_python//python:py_library.bzl", "py_library")
load("@rules_python//python:py_test.bzl", "py_test")
load("@py_deps//:requirements.bzl", "requirement")

py_library(
    name = "rest_client",
    srcs = ["rest_client.py"],
    deps = [requirement("aiohttp")],
)

py_test(
    name = "test_rest_client",
    srcs = ["test_rest_client.py"],
    deps = [":rest_client"],
)
