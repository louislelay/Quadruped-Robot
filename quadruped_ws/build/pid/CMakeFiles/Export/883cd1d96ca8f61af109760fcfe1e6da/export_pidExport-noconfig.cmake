#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "pid::pid" for configuration ""
set_property(TARGET pid::pid APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(pid::pid PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_NOCONFIG "CXX"
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libpid.a"
  )

list(APPEND _cmake_import_check_targets pid::pid )
list(APPEND _cmake_import_check_files_for_pid::pid "${_IMPORT_PREFIX}/lib/libpid.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
