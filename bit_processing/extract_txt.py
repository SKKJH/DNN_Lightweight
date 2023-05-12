import os
import shutil
import sys


# 원본 폴더와 대상 폴더 경로 설정
filename = sys.argv[1]

src_folder = 'saveorigin_' + filename
dst_folder = 'saveorigin_' + filename + '_only_txt'


# 대상 path 없으면 새로 생성
if not os.path.exists(dst_folder):
    os.makedirs(dst_folder)

dst_folder_shift = './shift/'
# 대상 폴더가 없으면 새로 생성
if not os.path.exists(dst_folder_shift):
    os.makedirs(dst_folder_shift)

# 원본 폴더 안의 모든 파일 검색
for root, _, files in os.walk(src_folder):
    for filename in files:
        # txt 파일인 경우만 선택
        if filename.endswith('.txt'):
            # txt 파일의 경로
            src_file_path = os.path.join(root, filename)
            # 저장될 파일이름 설정(앞의 폴더이름 지우기)
            # /를 __ 로 바꾸기
            root_num = len(src_folder)
            new_file_name = src_file_path[root_num:].replace('/', '__')
            # 대상 폴더에 파일 복사
            print(dst_folder+new_file_name)
            shutil.copy(src_file_path, dst_folder+'/'+new_file_name)
