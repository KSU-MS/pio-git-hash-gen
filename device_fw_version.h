#ifndef __DEVICE_FW_VERSION__
#define __DEVICE_FW_VERSION__
#include <stdint.h>
#include <cstddef>
#include <stdio.h>

#ifndef AUTO_VERSION
#warning "AUTO_VERSION was not defined by the generator!"
#define AUTO_VERSION 0xdeadbeef
#endif
#ifndef FW_PROJECT_IS_DIRTY
#warning "FW_PROJECT_IS_DIRTY was not defined by the generator!"
#define FW_PROJECT_IS_DIRTY 1
#endif
#ifndef FW_PROJECT_IS_MAIN_OR_MASTER
#warning "FW_PROJECT_IS_MAIN_OR_MASTER was not defined by the generator!"
#define FW_PROJECT_IS_MAIN_OR_MASTER 0
#endif

// ideally little endian bc teensy
struct device_status_t
{
    const uint32_t firmware_version = AUTO_VERSION;
    const bool project_on_main_or_master = FW_PROJECT_IS_MAIN_OR_MASTER;
    const bool project_is_dirty = FW_PROJECT_IS_DIRTY;
};

std::array<char, 8> convert_version_to_char_arr(uint32_t hex_ver)
{
    std::array<char, 8> ver_str;
    (void)snprintf(ver_str.data(), 8, "%x", hex_ver);
    return ver_str;
}

#endif