import requests
import os

url_for_deepl = 'https://api-free.deepl.com/v2/translate'

# 파일을 읽기 위한 디렉토리 경로를 설정합니다
directory = "./dataset/HumanML3D/texts/"
target_directory = "./dataset/HumanML3D/texts_ko"
file_name = []
with open("./dataset/HumanML3D/all.txt", 'r') as index_file:
    for line in index_file:
        # 파일 이름을 정리합니다.
        filename = line.strip()  # 줄 바꿈 문자를 제거합니다.
        file_name.append(filename)
        # txt 파일을 읽습니다.

for idx, name in enumerate(file_name):
    if idx>4866:
        with open(directory + name + '.txt', 'r', encoding='utf-8') as txt_file:
            for sentence in txt_file:
                content = sentence.split("#")[0]
                f_tag = sentence.split("#")[2]
                to_tag = sentence.split("#")[3]
                params = {'auth_key' : 'd9712eb7-102d-70cb-9c0c-75c98dd6f0d9:fx', 'text' : content, 'source_lang' : 'EN', "target_lang": 'KO' }           
                result = requests.post(url_for_deepl, data=params, verify=False)
                with open(os.path.join(target_directory, f"{name}.txt"), 'a', encoding='utf-8') as target:
                    target.write(result.json()['translations'][0]["text"] + '#' + f_tag + '#' + to_tag)
                    # target.write(content + '#' + f_tag + '#' + to_tag)
            
# message = 'Good afternoon and have a nice lunch'
# params = {'auth_key' : '809ff941-eefe-7fa3-008d-5f8f3c3de41b:fx', 'text' : message, 'source_lang' : 'EN', "target_lang": 'KO' }

# result = requests.post(url_for_deepl, data=params, verify=False)

# print(result.json()['translations'][0]["text"])