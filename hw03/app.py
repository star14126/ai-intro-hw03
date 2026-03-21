import streamlit as st
from PIL import Image, ImageDraw
from src.face_utils import detect_faces, get_face_encodings

# 页面配置
st.set_page_config(page_title="人脸检测", page_icon="👤")
st.title("👤 人脸检测系统")

# 选择图片来源
option = st.radio("选择图片来源", ["上传图片", "使用示例图片"])

image = None
if option == "上传图片":
    uploaded_file = st.file_uploader("上传一张图片", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image = Image.open(uploaded_file)
else:
    # 示例图片：把一张人脸照片放进 tests 文件夹，命名为 sample.jpg
    try:
        image = Image.open("tests/sample.jpg")
    except:
        st.warning("示例图片不存在，请上传图片！")

# 显示原始图片
if image:
    st.subheader("原始图片")
    st.image(image, use_column_width=True)

    # 人脸检测
    st.subheader("检测结果")
    face_locations = detect_faces(image)
    
    if face_locations:
        st.success(f"✅ 检测到 {len(face_locations)} 张人脸")
        # 在图片上画框
        draw = ImageDraw.Draw(image)
        for (top, right, bottom, left) in face_locations:
            draw.rectangle([(left, top), (right, bottom)], outline="red", width=3)
        st.image(image, caption="带人脸框的结果", use_column_width=True)
        
        # 可选：显示特征编码
        if st.checkbox("显示人脸特征编码"):
            encodings = get_face_encodings(image)
            for i, enc in enumerate(encodings):
                st.text(f"人脸 {i+1} 编码前10位: {enc[:10]}...")
    else:
        st.info("ℹ️ 未检测到人脸")