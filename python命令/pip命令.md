# pip 命令

> `pip` 是 Python 的包管理工具，用于安装、查看和卸载第三方库（包）

## 基本命令

### 查看包

```shell
pip list  # 查看全部

pip show package_name  # 查看指定包详细信息
```

### 安装包

```shell
pip install package_name  # 默认最新的

pip install package_name==版本号  # 指定版本安装
```

### 升级包

> 升级为最新版本

```shell
pip install --upgrade package_name
```

### 卸载包

> 默认只卸载指定包，不会自动删除其依赖包
> 在虚拟环境中，如果依赖关系复杂，通常更推荐直接删除虚拟环境后重新创建

```shell
pip uninstall package_name
```

## pip 镜像源

### 国内推荐镜像地址

- 阿里云：https://mirrors.aliyun.com/pypi/simple
- 清华大学：https://pypi.tuna.tsinghua.edu.cn/simple

### 通过镜像源安装库

```shell
pip install package_name -i https://mirrors.aliyun.com/pypi/simple
```

### 设置镜像源为全局默认

```shell
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
```

### 查看镜像源

```shell
pip config list
```
