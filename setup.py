from setuptools import setup, find_packages

setup(
    include_package_data = True,
    name = 'DataStructureCol',
    # 프로젝트 명을 입력합니다.
    version = '0.0.1',
    # 프로젝트 버전을 입력합니다.
    url = "https://github.com/YGC20/DataSort",
    # 홈페이지 주소를 입력합니다.
    author = 'YGC20',
    # 프로젝트 담당자 혹은 작성자를 입력합니다.
    author_email = 'ygchun123@naver.com',
    # 프로젝트 담당자 혹은 작성자의 이메일 주소를 입력합니다.
    description = 'This is pip, which is a collection of functions used for data structures.',
    # 프로젝트에 대한 간단한 설명을 입력합니다.
    packages = find_packages(exclude=['tests']),
    # 기본 프로젝트 폴더 외에 추가로 입력할 폴더를 입력합니다.
    long_description=open('README.md').read(), 
    # 프로젝트에 대한 설명을 입력합니다. 보통 README.md로 관리합니다.
    long_description_content_type='text/markdown', 
    # 마크다운 파일로 description를 지정했다면 text/markdown으로 작성합니다.
    install_requires=[''],
    # 설치시 설치할 라이브러리를 지정합니다.
    zip_safe=False,
    classifiers=[
        "Programming Language :: Pyton"
        "License :: OSI Approved :: MIT License"
    ],
)