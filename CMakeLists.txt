cmake_minimum_required( VERSION 2.6 )

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


project(casa_source)

set( BRAINVISA_COMPONENTS
    soma-base
    soma-io
    aims-free
    aims-gpl
    anatomist-free
    anatomist-gpl
    soma-workflow
    axon
    bioprocessing
    brainrat-gpl
    brainrat-private
    3dns-private
    brainvisa-cmake
    brainvisa_freesurfer
    brainvisa-share
    brainvisa-spm
    capsul
    casa-distro
    # cati-auth
    catidb-client
    # catidb-server
    constellation-gpl
    constellation-nonfree
    cortical_surface-gpl
    cortical_surface-nonfree
    disco
    highres-cortex
    longitudinal_pipelines
    morpho-deepsulci
    morphologist-baby
    morphologist-gpl
    morphologist-nonfree
    morphologist-ui
    nuclear_imaging-gpl
    nuclear_imaging-nonfree
    populse_db
    preclinical-imaging-iam
    qualicati
    rsfmri
    sacha-gpl
    sacha-nonfree
    sulci-nonfree
    web
    whasa-gpl
    whasa-nonfree

    CACHE STRING "Components list" FORCE )

set( _BRAINVISA_COMPONENTS "${BRAINVISA_COMPONENTS}" CACHE STRING "BrainVISA components list" FORCE )

set( CMAKE_PREFIX_PATH "${CMAKE_SOURCE_DIR}/brainvisa-cmake/cmake" ${CMAKE_PREFIX_PATH} )
find_package( brainvisa-cmake NO_POLICY_SCOPE )

foreach( component ${BRAINVISA_COMPONENTS} )
    set( BRAINVISA_SOURCES_${component} "${CMAKE_SOURCE_DIR}/${component}" CACHE STRING "Sources directory for component ${component}" FORCE )
    BRAINVISA_READ_PROJECT_INFO("${BRAINVISA_SOURCES_${component}}")
    set( ${component}_VERSION "${BRAINVISA_PACKAGE_VERSION_MAJOR}.${BRAINVISA_PACKAGE_VERSION_MINOR}" )
    set( ${component}_DIR "${CMAKE_BINARY_DIR}/share/${component}-${${component}_VERSION}/cmake" CACHE STRING "Directory used for find_package( ${component} )" FORCE )
endforeach()

include( "${BRAINVISA_SOURCES_brainvisa-cmake}/cmake/brainvisa-compilation.cmake" )
