from conans import ConanFile, CMake, tools
import os


class RobotConan(ConanFile):
    name = "Robot"
    version = "2.0"
    license = "MIT"
    url = "https://github.com/memsharded/conan-robot"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone https://github.com/Sqeaky/robot.git")
        tools.replace_in_file("robot/CMakeLists.txt", "project(Robot)", """project(Robot)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
""")

    def build(self):
        cmake = CMake(self.settings)
        shared = "-DBuildStatic=OFF" if self.options.shared else "-DBuildStatic=ON"
        self.run('cmake robot %s %s' % (cmake.command_line, shared))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="robot/Source")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Robot"]
