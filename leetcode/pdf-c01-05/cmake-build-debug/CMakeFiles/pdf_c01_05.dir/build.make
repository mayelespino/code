# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.6

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /Applications/CLion.app/Contents/bin/cmake/bin/cmake

# The command to remove a file.
RM = /Applications/CLion.app/Contents/bin/cmake/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/mayelespino/Repos/code/leetcode/pdf-c01-05

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/pdf_c01_05.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/pdf_c01_05.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/pdf_c01_05.dir/flags.make

CMakeFiles/pdf_c01_05.dir/main.cpp.o: CMakeFiles/pdf_c01_05.dir/flags.make
CMakeFiles/pdf_c01_05.dir/main.cpp.o: ../main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/pdf_c01_05.dir/main.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++   $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/pdf_c01_05.dir/main.cpp.o -c /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/main.cpp

CMakeFiles/pdf_c01_05.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/pdf_c01_05.dir/main.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/main.cpp > CMakeFiles/pdf_c01_05.dir/main.cpp.i

CMakeFiles/pdf_c01_05.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/pdf_c01_05.dir/main.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/main.cpp -o CMakeFiles/pdf_c01_05.dir/main.cpp.s

CMakeFiles/pdf_c01_05.dir/main.cpp.o.requires:

.PHONY : CMakeFiles/pdf_c01_05.dir/main.cpp.o.requires

CMakeFiles/pdf_c01_05.dir/main.cpp.o.provides: CMakeFiles/pdf_c01_05.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/pdf_c01_05.dir/build.make CMakeFiles/pdf_c01_05.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/pdf_c01_05.dir/main.cpp.o.provides

CMakeFiles/pdf_c01_05.dir/main.cpp.o.provides.build: CMakeFiles/pdf_c01_05.dir/main.cpp.o


# Object files for target pdf_c01_05
pdf_c01_05_OBJECTS = \
"CMakeFiles/pdf_c01_05.dir/main.cpp.o"

# External object files for target pdf_c01_05
pdf_c01_05_EXTERNAL_OBJECTS =

pdf_c01_05: CMakeFiles/pdf_c01_05.dir/main.cpp.o
pdf_c01_05: CMakeFiles/pdf_c01_05.dir/build.make
pdf_c01_05: CMakeFiles/pdf_c01_05.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable pdf_c01_05"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pdf_c01_05.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/pdf_c01_05.dir/build: pdf_c01_05

.PHONY : CMakeFiles/pdf_c01_05.dir/build

CMakeFiles/pdf_c01_05.dir/requires: CMakeFiles/pdf_c01_05.dir/main.cpp.o.requires

.PHONY : CMakeFiles/pdf_c01_05.dir/requires

CMakeFiles/pdf_c01_05.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/pdf_c01_05.dir/cmake_clean.cmake
.PHONY : CMakeFiles/pdf_c01_05.dir/clean

CMakeFiles/pdf_c01_05.dir/depend:
	cd /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/mayelespino/Repos/code/leetcode/pdf-c01-05 /Users/mayelespino/Repos/code/leetcode/pdf-c01-05 /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug /Users/mayelespino/Repos/code/leetcode/pdf-c01-05/cmake-build-debug/CMakeFiles/pdf_c01_05.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/pdf_c01_05.dir/depend

