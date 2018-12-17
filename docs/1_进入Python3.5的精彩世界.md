# 进入 Python3.5 的精彩世界

## Python 的应用场合

Python 的哲学，简单、优雅、明确。

## 从 2.7 到 3.5，Python 新特性

两个版本的主要区别：

### 使用 **future**模块

在 py2 里，可以使用 **future** 来使用新内容

### print 函数

在 py3 里，print() 是函数调用

### 整数除法

### Unicode

py3 有 Unicode 字符串，和 bytes bytearrays

### xrange

py3 里使用 range()

### 触发异常

py3 只支持带括号的语法

### 处理异常

py3 必须使用 as 关键字

### next() 函数 .next()方法

在 py3 里，只能使用 next()函数

### for 循环变量和全局命名空间的泄露

py3 里 for 循环变量不会泄露到全局命名空间

### 比较无序类型

py3 不能比较无序类型

### input() 输入

py3 里 input() 函数储存为 str，避免了危险行为

### 返回可迭代对象，不是列表

返回可迭代对象，而不是 py2 的列表，省内存，用 list()转换为列表很方便
