# 메이플스토리 코어강화 보조 시스템

### 개발동기
- 메이플 스토리 5차 전직 이후 사용할 수 있는 V매트릭스의 어려움을 겪어 조금이나마 개선해보고자 개발

![image](https://github.com/user-attachments/assets/d0c7baa5-036a-4b3a-b085-e992be76cc31)
- V매트릭스는 이미지와 같이 스킬코어와 강화코어, 특수코어로 나누어져 있다.

![image](https://github.com/user-attachments/assets/96b4a393-19b6-411e-ba34-6ef223c98caf)
- 강화코어는 위 이미지와 같이 이전에 배웠던 스킬들을 강화해주는 개념으로 3개의 스킬이 합쳐져 있는 형태
- 이전에 배웠던 모든 스킬을 강화해주는 것이 아니라 필요로 하는 스킬들만 강화해주는 방식으로 하기에 스킬이 적절하게 중첩되게 하여 배치하는 것이 중요

![image](https://github.com/user-attachments/assets/aaa5bcf2-1df9-4453-99dc-4dad98a4e429)
- 필요로 하는 스킬들은 나무위키나 구글링을 통해 쉽게 알아볼 수 있다.(사람마다 차이가 있기에 꼭 저걸 따르진 않아도 된다.)
- *추후 나무위키 크롤링을 통해 필요스킬들도 얻을 수 있는 코드를 작성할 예정

### 코드
#### 변수
main - 5차 이전에 배웠던 필요 스킬
skill - 현재 내가 갖고있는 강화코어(5차 이전에 배웠던 스킬 3가지의 조합)
m - 사용할 코어칸 수
n - main에 있는 스킬들의 중첩 횟수
#### 코어강화 조건
- m개의 코어강화 칸을 사용하여 main의 모든 강화스킬들이 n번씩 중첩되게 만들어 주어야 한다.
- 추출해낸 스킬 리스트의 첫번째 원소가 같으면 안된다.
#### 코드 설명
- is_valid_combination(comb):

선택된 조합(comb)에서 main의 모든 원소가 정확히 n번씩 나타나는지 검사합니다. 
- 조합 생성 및 검증:

skill 리스트에서 가능한 모든 m개의 조합을 생성합니다. 각 조합의 첫 번째 원소가 서로 다른지 확인하고, 유효한 조합을 리스트에 저장합니다. 
- 결과 반환:

유효한 조합이 있으면 그 조합들을 리스트로 반환하고, 없으면 "경우의 수가 없습니다."라는 메시지를 반환합니다. 위 코드는 주어진 조건을 충족하는 모든 조합을 찾고 출력합니다. 각 조합이 main 리스트의 모든 원소가 n번씩 나타나는지 확인하고, 첫 번째 원소가 겹치지 않는지 확인하여 유효한 조합만을 출력합니다.

### 개선점
- 현재 갖고있는 코어들을 다 작성하려다보니 손이 많이가는 문제점 발생
- 현재 개발해둔 코드들은 skill 데이터엔 main의 원소들로 이루어진 스킬들만 존재하지만 나중엔 모든 skill 데이터를 집어넣어 할 수 있을 여지가 있다.
- 현재는 간단하게 파악하기 위하여 숫자로 입력하였지만, 한글 이름으로도 되는지 체크해야 한다.
- Nexon API를 통해 개인 캐릭터에 대한 정보를 얻어 main 스킬, n중첩, m코어칸만 입력하여 간단하게 사용할 수 있는 여지가 있다.

24.08.23 Combination 라이브러리를 활용한 코드 추가 업로드
