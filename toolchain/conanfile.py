mport os
from conans import ConanFile
from conans.client import tools


class ECUConan(ConanFile):
    name = "ecu_sdk"
    revision = "R04"
    version = "2.7.2.220"
    platform = "platty"
    license = "BSD-2-Clause"
    settings = "os_build", "arch_build"
    arch = "armv7"
    build_policy = "missing"
    description = "ECU SDK for linux. Builds for 400-level ACMs."
    svnServer = "corp.com"
    svnAddress = "http://" + svnServer + "/svn"
    svnRepo = svnAddress + "/ECU/trunk/SDK/TAR_Files"
    svnURL = svnRepo + "/%s_sdk_%s_%s" % (platform, version, "R05")
    url = svnURL
    ccPrefix = "arm-linux-gnueabihf"
    installRoot = "/opt/ecu"
    installPath = os.path.join(installRoot, revision)
    workingDir = os.path.join( installPath, "platform", platform, "release")


    def package(self):
        self.copy("*", dst="", keep_path=True)


    def package_info(self):
        bin_folder = os.path.join( self.workingDir + "/toolchain/usr/bin" )
        self.output.warn( "setting bin folder " + bin_folder)
        self.env_info.PATH.append(bin_folder)
        self.env_info.CC = os.path.join(bin_folder, self.ccPrefix + "-gcc")
        self.env_info.CXX = os.path.join(bin_folder, self.ccPrefix + "-g++")
        self.env_info.CPP = os.path.join(bin_folder, self.ccPrefix + "-cpp")
        self.env_info.LD = os.path.join(bin_folder, self.ccPrefix + "-ld")
        self.env_info.AR = os.path.join(bin_folder, self.ccPrefix + "-ar")
        self.env_info.GDB = os.path.join(bin_folder, self.ccPrefix + "-gdb")
        self.env_info.SYSROOT = os.path.join( self.installPath, "/toolchain/usr/", self.ccPrefix, "/sysroot")
        self.cpp_info.includedirs = [ os.path.join( self.workingDir, 'include', 'libascommon'), os.path.join( self.workingDir, 'include', 'libashal'), os.path.join( self.workingDir, 'include', 'libasiso'), os.path.join( self.workingDir, 'include', 'libaspresentation')]
        self.cpp_info.cxxflags = [ '-L' + os.path.join(self.workingDir, '/lib'), '-L' + os.path.join(self.workingDir, 'third-party/lib') ]
