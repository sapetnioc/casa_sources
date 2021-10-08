cmake_minimum_required( VERSION 3.0 )

project( casa_source C CXX Fortran )

list( INSERT CMAKE_PREFIX_PATH  0 "${CMAKE_BINARY_DIR}/cmake" "${CMAKE_SOURCE_DIR}/brainvisa-cmake/cmake" )
list( INSERT CMAKE_MODULE_PATH 0 "${CMAKE_SOURCE_DIR}/brainvisa-cmake/cmake/modules" )

find_package( python 3 )

# Replacement of BRAINVISA_PROJECT
macro( THIS_PROJECT project_name )
    if( CMAKE_MAJOR_VERSION GREATER 2 )
        cmake_policy(SET CMP0048 OLD)
    endif()
    project(${project_name})
    set( _run_install "False" )
    set( _dev_install "False" )
    set( _usrdoc_install "False" )
    set( _devdoc_install "False" )
    set( _doc_install "False" )
    set( _test_install "False" )

    set( ${PROJECT_NAME}_TARGET_COUNT 0 CACHE INTERNAL "Used to generate new targets" )
    set( ${PROJECT_NAME}-commands "" CACHE INTERNAL "Commands list for component ${PROJECT_NAME}" )
    BRAINVISA_CREATE_MAIN_COMPONENTS()

    set( CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin" )
    set( CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib" )
endmacro()

# Read components list
execute_process(COMMAND ${PYTHON_EXECUTABLE} read_components.py
                WORKING_DIRECTORY "${CMAKE_SOURCE_DIR}"
                OUTPUT_VARIABLE BRAINVISA_COMPONENTS
                ERROR_VARIABLE stderr
                RESULT_VARIABLE status)

if( NOT ${status} EQUAL 0) 
    message("ERROR while running ${CMAKE_SOURCE_DIR}/read_components.py")
    message( FATAL_ERROR "${stderr}")
endif()

set( NO_BV_MAKER TRUE CACHE STRING "Compilation without using bv_maker command" FORCE )
# set( _BRAINVISA_COMPONENTS "${BRAINVISA_COMPONENTS}" CACHE STRING "BrainVISA components list" FORCE )

find_package( brainvisa-cmake NO_POLICY_SCOPE )

# Necessary for BRAINVISA_READ_PROJECT_INFO
file( MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/build_files" )

foreach( component ${BRAINVISA_COMPONENTS} )
    set( BRAINVISA_SOURCES_${component} "${CMAKE_SOURCE_DIR}/${component}" CACHE STRING "Sources directory for component ${component}" FORCE )
    BRAINVISA_READ_PROJECT_INFO("${BRAINVISA_SOURCES_${component}}")
    set( ${component}_VERSION "${BRAINVISA_PACKAGE_VERSION_MAJOR}.${BRAINVISA_PACKAGE_VERSION_MINOR}" )
    set( ${component}_DIR "${BRAINVISA_SOURCES_${component}}/share/cmake" CACHE STRING "Directory used for find_package( ${component} )" FORCE )
    file( MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/share/${component}-${${component}_VERSION}" )
    execute_process( COMMAND ${CMAKE_COMMAND} -E create_symlink "../../cmake" "${CMAKE_BINARY_DIR}/share/${component}-${${component}_VERSION}/cmake" )
endforeach()

include( "${BRAINVISA_SOURCES_brainvisa-cmake}/cmake/brainvisa-compilation.cmake" )
