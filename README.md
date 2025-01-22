# dmcount_function

## 项目概述
dmcount_function 是一个用于统计C++函数编译后汇编代码行数的工具。它支持在Windows（MSVC）和Linux/Mac（GCC）环境下运行，能够自动检测编译器环境并生成相应的汇编代码统计。

## 功能特点
- 自动检测编译器环境（MSVC/GCC）
- 支持跨平台使用
- 统计指定函数的汇编代码行数
- 提供Windows（.bat）和Linux/Mac（.sh）的快捷调用方式

## 安装要求
- Python 3.x
- C++编译器（MSVC或GCC）
- 目标平台开发工具链（如Windows SDK或GNU工具链）

## 使用说明
1. 确保已安装所需的编译器和Python环境
2. 在项目目录下运行：
   - Windows: `count.bat`
   - Linux/Mac: `./count.sh`
3. 程序将输出指定函数的汇编代码行数

## 文件说明
- `count_asm.py`: 主程序，实现汇编代码统计功能
- `main.cc`: 示例C++源文件，包含mysort函数
- `count.bat`: Windows批处理脚本
- `count.sh`: Linux/Mac shell脚本
- `LICENSE`: 项目许可证文件

## 贡献指南
欢迎提交Pull Request或Issue。请确保：
1. 代码风格与现有代码一致
2. 添加适当的测试用例
3. 更新相关文档

## 许可证
本项目采用MIT许可证，详情请参阅LICENSE文件。
