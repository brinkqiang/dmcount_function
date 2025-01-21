import subprocess
import sys
import os
import platform

def detect_compiler():
    """自动检测当前使用的编译器环境"""
    if platform.system() == "Windows":
        # 在 Windows 上检查 MSVC
        if "cl" in subprocess.run("where cl", shell=True, capture_output=True, text=True).stdout:
            return "msvc"
    # 默认认为是 GCC 环境
    return "gcc"

def compile_cpp_file(cpp_file, compiler):
    """根据编译器选择编译命令"""
    if compiler == "msvc":
        # 使用 MSVC 编译 C++ 文件
        compile_command = [
            "cl", "/EHsc", "/Fo", "main.obj", "/c", cpp_file
        ]
    else:
        # 使用 GCC 编译 C++ 文件
        compile_command = [
            "g++", "-g", "-O0", "-std=c++17", "-c", cpp_file, "-o", "main.o"
        ]
    subprocess.run(compile_command, check=True)

def count_asm_lines(binary_file, function_name, compiler):
    """根据编译器环境使用不同工具进行反汇编并统计函数的汇编行数"""
    try:
        if compiler == "msvc":
            # MSVC 环境使用 dumpbin 进行反汇编
            result = subprocess.run(
                ["dumpbin", "/disasm", binary_file],
                text=True,
                capture_output=True,
                check=True
            )
        else:
            # GCC 环境使用 objdump 进行反汇编
            result = subprocess.run(
                ["objdump", "-d", binary_file],
                text=True,
                capture_output=True,
                check=True
            )

        asm_code = result.stdout
        # 查找目标函数的汇编代码
        start_flag = f"<{function_name}>:"
        lines = asm_code.splitlines()
        count = 0
        inside_function = False

        for line in lines:
            if start_flag in line:
                inside_function = True
                continue
            if inside_function:
                # 遇到空行或其他符号，认为函数结束
                if line.strip() == "" or not line.startswith(" "):
                    break
                # 统计实际指令行
                count += 1

        return count
    except subprocess.CalledProcessError as e:
        print("Error running disassembler:", e)
        return -1

def main():
    if len(sys.argv) != 3:
        print("Usage: python count_asm.py <C++ source file> <function name>")
        sys.exit(1)

    cpp_file = sys.argv[1]
    function_name = sys.argv[2]

    if not os.path.exists(cpp_file):
        print(f"Error: The file '{cpp_file}' does not exist.")
        sys.exit(1)

    # 检测当前的编译器环境
    compiler = detect_compiler()
    print(f"Detected compiler: {compiler}")

    # 编译 C++ 文件
    print(f"Compiling {cpp_file}...")
    compile_cpp_file(cpp_file, compiler)

    # 选择正确的目标文件（MSVC 使用 .obj，GCC 使用 .o）
    binary_file = "main.obj" if compiler == "msvc" else "main.o"

    # 统计汇编代码行数
    print(f"Analyzing assembly code for function '{function_name}'...")
    line_count = count_asm_lines(binary_file, function_name, compiler)

    if line_count >= 0:
        print(f"Function '{function_name}' has {line_count} assembly lines.")
    else:
        print("Failed to analyze the binary file.")

if __name__ == "__main__":
    main()
