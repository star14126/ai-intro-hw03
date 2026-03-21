# 人脸检测与识别作业

## 项目结构
hw03/
├── src/face_utils.py # 人脸检测与特征提取核心代码
├── app.py # Streamlit Web 界面
├── requirements.txt # 依赖清单
├── tests/ # 测试图片目录
└── README.md # 项目说明

## 功能说明
1. 支持上传图片或使用示例图片
2. 自动检测人脸并框选显示
3. 可选展示人脸128维特征编码

## 环境安装
```bash
pip install -r requirements.txt
## 运行方式
```bash
streamlit run app.py
访问 http://localhost:8501 即可使用。