#!/usr/bin/env python
from cx_Freeze import setup,  Executable

setup(
    version = "0.3",
    description = "MS JavaLoader",
    name = "MSJL-BB",

    # targets to build
    executables = [Executable(script="jl.pyw", 
                              icon="JL_Cmder.ico",  base="Win32GUI")],
    )

