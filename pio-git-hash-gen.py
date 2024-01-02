import pkg_resources

Import("env")
required_pkgs = {'dulwich'}
installed_pkgs = {pkg.key for pkg in pkg_resources.working_set}
missing_pkgs = required_pkgs - installed_pkgs

if missing_pkgs:
    env.Execute('$PYTHONEXE -m pip install dulwich --global-option="--pure"')

from dulwich import porcelain

def get_firmware_specifier_build_flag():
    build_version = porcelain.describe('.')  # '.' refers to the repository root dir
    print(build_version)
    return (build_version)


env.Append(CPPDEFINES=[
    ("AUTO_VERSION",env.StringifyMacro(get_firmware_specifier_build_flag()))
]
)