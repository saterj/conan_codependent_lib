from conans import ConanFile, CMake
import os

class UtilitiesConanConan(ConanFile):
    name = "conan_codependent"
    version = "trunk"
    license = "nunya.1.0"
    url = os.path.join("http://server.com/svn/Parts_Store/trunk/ECU", name)
    description = "a utility lib"
    exports_sources = "src/*", "CMakeLists.txt" 
    no_copy_source = True
    generators = "cmake"
    
    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="conan_run.log", dst="", keep_path=False)
        self.copy("*.h")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
    
    def build_requirements(self):
        self.build_requires("HeaderOnly/trunk@Parts_Store/test")

    def package_info(self):
        self.output.warn( self.env_info )
        self.cpp_info.includedirs = [ 'src' ]
