#!/usr/bin/env bash

srcPath=../../../labs/01-build-your-own
targetDir="target"

# Make sure target directory exists
mkdir --parents "${targetDir}"

# Compile HelloWorldApp.java to target directory
javac \
    -sourcepath "${srcPath}" \
    -d "${targetDir}" \
    "${srcPath}/com/bol/lab/HelloWorldApp.java"

# Run compiled version of HelloWorldApp
java \
    -cp ${targetDir} \
    com/bol/lab/HelloWorldApp
