# 폴더에서 실행
# 자동으로 .git 폴더 삭제 해주는 코드
# 현재 폴더를 기준으로 모든 폴더를 조사
# .git 폴더를 삭제한다
    # 단, 최상위 폴더 (코드가 실행된 위치의 .git은 제외하고)
# os : PSL -> 운영체제와 상호작용 가능
import os
import subprocess

# get current working directory
# print(os.getcwd())

# # change directory
# os.chdir('01_python/')
# print(os.getcwd())
# os.removedirs

# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()

# 현재 폴더 및 모든 하위 폴더를 반복
for foldername, subfolders, filenames in os.walk(current_folder):
    # print(foldername, 'fn')
    # print(subfolders, 'sf')
    # print(filenames, 'fn')
    # 하위 폴더 목록에 .git이 있다면
    if '.git' in subfolders:
        # root directory는 제외
        if foldername == current_folder:
            continue  # 아래 코드 실행 말고 다음 순회
        # 그 외 모든 경우 .git 폴더 모두 삭제
        # 삭제하려는 .git 폴더의 위치를 변수에 저장
        git_folder_path = os.path.join(foldername, '.git')
        # 경로에는 '/' 를 사용
        # print(git_folder_path)
        # print(foldername)
        # print(subfolders)
        # 명령 프롬프트 실행
        # rm -rf 폴더 경로
        subprocess.run(['rm', '-rf', git_folder_path])
        print(f'{git_folder_path} 폴더가 삭제되었습니다.')