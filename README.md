# Skin-electrical-signal-state-judgment-tool-based-on-support-vector-machine-model
Built on SVM algorithm, this tool extracts features from electrodermal activity (EDA) data to identify 3 emotional states (baseline/pleasure/stress), and supports custom binary/ternary classification for personalized needs.

## Environment Requirements

### Hardware

- Processor: Intel Core i5+/AMD Ryzen 5+

- Memory: ≥8GB RAM

- Storage: ≥20GB free space (x86 architecture)

### Software

- OS: Windows 7+/macOS 10.15+/Linux (x86_64)

- Runtime: PyCharm + Python 3.12

- Dependencies: scikit-learn/pandas/numpy (install via requirements.txt)

## Core Workflow

1. Extract feature vectors from raw EDA CSV data

2. Preprocess features and train SVM model (retrain optional)

3. Batch predict new EDA data and output recognition results

## Custom Classification Setup

1. Place custom EDA CSV data into data folder

2. Modify eda_svm.py to replace default emotional labels

3. For binary classification: Delete the 3rd category's code/config

4. Re-run model training to apply changes

## Quick Start

### Model Training

1. Put training CSV files into data folder

2. Run eda_svm.py (model saved automatically)

### Emotion Prediction

1. Rename EDA CSV to 1.csv and put into han_experiment_test

2. Run main.py for batch prediction

3. Check results in result folder

## Notes

- Refer to the user manual and demonstration video in the project for detailed guidance

- Ensure prediction data is CSV (same structure as training data)

- Avoid Chinese/special characters in file paths/names

- For binary classification: Remove the 3rd class config to prevent training errors

## About the Author & Project Declaration

- Affiliation: Delaware State University (特拉华州立大学)

- Project Owner: This tool is independently developed and maintained by Zhang Hanwen , for academic research use.

- Contact Email: 18583074836@163.com

---

# 基于支持向量机模型的皮肤电信号状态判断工具

本工具基于支持向量机（SVM）算法构建，可从皮肤电反应（EDA）数据中提取特征，识别3种情绪状态（基线状态/愉悦状态/压力状态），并支持自定义二分类/三分类设置，以满足个性化需求。

## 环境要求

### 硬件要求

- 处理器：Intel Core i5及以上/AMD Ryzen 5及以上

- 内存：≥8GB

- 存储：≥20GB可用空间（x86架构）

### 软件要求

- 操作系统：Windows 7及以上/macOS 10.15及以上/Linux（x86_64架构）

- 运行环境：PyCharm + Python 3.12

- 依赖库：scikit-learn/pandas/numpy（通过requirements.txt文件安装）

## 核心工作流程

1. 从原始EDA CSV数据中提取特征向量

2. 对特征进行预处理并训练SVM模型（可选择重新训练）

3. 对新的EDA数据进行批量预测，并输出识别结果

## 自定义分类设置

1. 将自定义EDA CSV数据放入data文件夹

2. 修改eda_svm.py文件，替换默认的情绪标签

3. 若为二分类：删除第三类的代码/配置

4. 重新运行模型训练，使修改生效

## 快速开始

### 模型训练

1. 将训练用CSV文件放入data文件夹

2. 运行eda_svm.py文件（模型将自动保存）

### 情绪预测

1. 将EDA CSV文件重命名为1.csv，并放入han_experiment_test文件夹

2. 运行main.py文件进行批量预测

3. 在result文件夹中查看预测结果

## 注意事项

- 详细操作指南请参考项目中的用户手册及演示视频

- 确保预测数据为CSV格式（与训练数据结构一致）

- 文件路径/名称中避免包含中文及特殊字符

- 若为二分类：请删除第三类的配置，避免训练报错

## 作者及项目声明

- 所属单位：特拉华州立大学（Delaware State University）

- 项目归属：本工具由本人独立开发与维护，用于学术研究用途。

- 联系邮箱：18583074836@163.com
​
