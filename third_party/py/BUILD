load("@rules_python//python:pip.bzl", "compile_pip_requirements")

compile_pip_requirements(
    name = "requirements",
    extra_args = ["--allow-unsafe"],
    requirements_in = "//third_party/py:requirements.txt",
    requirements_txt = "//third_party/py/private/generated:requirements.txt",
)

alias(
    name = "update",
    actual = "@//third_party/py:requirements.update"
)
