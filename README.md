# LazyScraper 项目说明

## 简介

> 用于 python AyugeSpiderTools 项目结构模版生成。

- 在创建 `scrapy` 项目时，每次都需要配置开发工具，测试工具，`CI/CD` 等内容，非常需要一种方式来快速创建项目模版；
- `AyugeSpiderTools` 项目现保持结构与 `scrapy` 一致，其他配置和运行等模版则通过此项目实现；
- 基于 `cookiecutter` 可以很方便地实现个性化项目模版的创建。

## 使用方式

```shell
# 需要提前安装好 `cookiecutter`
pip install cookiecutter

# 然后根据 repo 模版生成项目
cookiecutter https://github.com/shengchenyang/LazyScraper.git
```

## 运行示例

> 使用方式示例：

![LazyScraper-use.png](./examples/LazyScraper-use.png)

> 结果示例：

![LazyScraper-result.png](./examples/LazyScraper-result.png)

# 补充

- 可以根据 `github` 上的各种 `cookiecutter` 模版方便地创建项目，也可以 `fork` 他人优秀的项目结构来自定义项目。
- 更多介绍及示例请在 `cookiecutter` 文档中查看。
