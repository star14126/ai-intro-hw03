import face_recognition
import numpy as np
from PIL import Image

def detect_faces(image: Image.Image) -> list:
    """
    检测图片中的所有人脸位置
    返回格式：[(top, right, bottom, left), ...]
    """
    # 把 PIL 图片转成 numpy 数组（face_recognition 要求的格式）
    img_array = np.array(image.convert("RGB"))
    # 调用 face_recognition 检测人脸
    face_locations = face_recognition.face_locations(img_array)
    return face_locations

def get_face_encodings(image: Image.Image) -> list:
    """
    提取所有人脸的 128 维特征编码
    返回格式：[编码1, 编码2, ...]
    """
    img_array = np.array(image.convert("RGB"))
    face_encodings = face_recognition.face_encodings(img_array)
    return face_encodings

def compare_faces(known_encodings: list, face_encoding: list, tolerance: float = 0.6) -> list:
    """
    比对人脸特征，返回是否匹配
    known_encodings：已知人脸库的编码列表
    face_encoding：待识别的人脸编码
    tolerance：相似度阈值（越小越严格）
    """
    matches = face_recognition.compare_faces(known_encodings, face_encoding, tolerance=tolerance)
    return matches