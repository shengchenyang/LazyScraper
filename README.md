# LazyScraper 项目说明

## 简介

> 用于 python AyugeSpiderTools 项目结构模版生成。

- 在创建 `scrapy` 项目时，每次都需要配置开发工具，测试工具，`CI/CD` 等内容，非常需要一种方式来快速创建项目模版；
- `AyugeSpiderTools` 创建的项目结构与 `scrapy` 保持一致，其他配置和运行等模版则可通过此项目实现；
- 基于 `cookiecutter` 可以很方便地实现个性化项目模版的创建。

注：此项目还处于完善和优化阶段，但主要功能都已经具备。若你有快速且方便地创建 `Scrapy` 模版的需求，还是非常具有参考价值的。

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
