import subprocess
Import("projenv")


def get_firmware_specifier_build_flag():
    path = str(projenv["PROJECT_DIR"])
    build_version = subprocess.run(
        ['git', '-C', path, 'rev-parse', '--short', 'HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    build_version.strip()
    print("VERSION: " + (build_version))
    return int(build_version, 16)


def get_project_main_or_master():
    path = str(projenv["PROJECT_DIR"])
    main_or_master = subprocess.run(
        ['git', '-C', path, 'rev-parse', '--abbrev-ref','HEAD'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    main_or_master.strip()
    project_is_main_or_master = ('main' in main_or_master.lower()) or ('master' in main_or_master.lower())
    print("MAIN OR MASTER: " + (main_or_master) + " BOOL: " + str(project_is_main_or_master))
    return int(project_is_main_or_master)


def get_project_is_dirty():
    path = str(projenv["PROJECT_DIR"])
    project_status = subprocess.run(
        ['git', '-C', path, 'status', '--porcelain'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    project_status.strip()
    project_is_dirty = (project_status != '')
    print("Project is dirty: " + str(project_is_dirty))
    print("Project status: " + project_status)
    return int(project_is_dirty)


fw_flag = get_firmware_specifier_build_flag()
project_is_dirty = get_project_is_dirty()
project_is_main_or_master = get_project_main_or_master()
projenv.Append(CPPDEFINES=[
    ("AUTO_VERSION", fw_flag),
    ("FW_PROJECT_IS_DIRTY", project_is_dirty),
    ("FW_PROJECT_IS_MAIN_OR_MASTER",project_is_main_or_master)
]
)
