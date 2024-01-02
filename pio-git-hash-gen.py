Import("projenv")
import subprocess

def get_firmware_specifier_build_flag():
    build_version  = subprocess.run(['git', 'rev-parse','--short', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    build_version.strip()
    print((build_version))
    return int(build_version,16)

fw_flag=get_firmware_specifier_build_flag()
projenv.Append(CPPDEFINES=[
    ("AUTO_VERSION",fw_flag)
]
)