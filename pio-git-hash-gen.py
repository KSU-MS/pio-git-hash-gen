Import("projenv")
import subprocess

def get_firmware_specifier_build_flag():
    path = str(projenv["PROJECT_DIR"])
    build_version  = subprocess.run(['git','-C',path, 'rev-parse','--short', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    build_version.strip()
    print("VERSION: " + (build_version))
    return int(build_version,16)

fw_flag=get_firmware_specifier_build_flag()
projenv.Append(CPPDEFINES=[
    ("AUTO_VERSION",fw_flag)
]
)