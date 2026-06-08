# 후배용 온보딩 가이드

이 문서는 다음 학기 또는 다음 팀이 프로젝트를 이어받을 때 가장 먼저 보면 되는 실행 안내입니다.

## 1. 먼저 볼 파일

1. `README.md`: 전체 프로젝트 설명
2. `docs/error_type_guide.md`: 오류 유형 기준
3. `data/student_profile_sample.csv`: 학생별 추천 모델 입력 예시
4. `data/student_error_sequence_sample.csv`: LSTM 오류 흐름 입력 예시
5. `notebooks/DKIS_math_mentoring_AI_model_pilot.ipynb`: Colab 실행 노트북

## 2. Colab 실행 순서

1. Colab에서 노트북을 엽니다.
2. `student_profile_sample.csv`와 `student_error_sequence_sample.csv`를 업로드합니다.
3. 셀을 위에서부터 차례대로 실행합니다.
4. 오류 유형 분포 그래프와 취약 단원 그래프를 확인합니다.
5. 규칙 기반 추천 결과를 확인합니다.
6. Random Forest Baseline 결과를 확인합니다.
7. LSTM 파일럿 결과를 확인합니다.
8. Manim 시각화용 데이터가 생성되는지 확인합니다.

## 3. 새 데이터를 추가할 때

새 학생 데이터를 추가하려면 반드시 기존 CSV 열 이름을 유지합니다.

### student_profile_sample.csv 형식

```csv
student_id,weak_topic,error_type,material_preference,difficulty_level
S01,함수,Strategy,예제,중
```

### student_error_sequence_sample.csv 형식

```csv
student_id,step,error_type,topic
S01,1,Process,함수
S01,2,Strategy,함수
S01,3,Micro,함수
```

## 4. 주의사항

- 실제 학생 이름은 쓰지 않습니다.
- 모델 결과를 최종 판단으로 사용하지 않습니다.
- 추천 결과는 멘토링 보조 자료로만 활용합니다.
- 데이터가 적은 경우 정확도보다 구조 확인에 의미를 둡니다.
