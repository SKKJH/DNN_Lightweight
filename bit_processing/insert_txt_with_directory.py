import os
import shutil
import sys

# 원본 폴더와 대상 폴더 경로 설정
filename = sys.argv[1]

src_folder = './shift'
dst_folder = 'saveshift_' + filename

# src_folder = 'save_incepRes_origin_only_txt'
# dst_folder = 'save_incepRes_shift'

# 대상 폴더가 없으면 새로 생성
if not os.path.exists(dst_folder):
    os.mkdir(dst_folder)

# 원본 폴더 안의 모든 파일 검색
for root, _, files in os.walk(src_folder):
    for filename in files:
        # txt 파일인 경우만 선택
        if filename.endswith('.txt') :# and filename[:4] == 'shift':
            src_file_path = os.path.join(root, filename)
            # 저장될 파일이름 설정(앞의 폴더이름 지우기)
            # __를 / 로 바꾸기
            print('src_file_path: ', src_file_path)
            root_num = len(src_folder)+1
            new_file_name = src_file_path[root_num:].replace('__', '/')
            print('new_file_name : ', new_file_name)
            dst_file_path = dst_folder+new_file_name
            print('dst_file_path: ', dst_file_path)
            print()
            # 대상 폴더에 파일 복사
            if not os.path.exists(os.path.dirname(dst_file_path)):
                os.makedirs(os.path.dirname(dst_file_path))
            shutil.copy(src_file_path, dst_file_path)
