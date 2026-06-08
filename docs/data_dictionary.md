# Data Dictionary

## student_profile_sample.csv

| Column | Meaning | Example |
|---|---|---|
| student_id | 익명 학생 ID | S01 |
| weak_topic | 학생이 어려워하는 단원 | 함수 |
| error_type | 대표 오류 유형 | Strategy |
| material_preference | 선호 자료 형태 | 예제 |
| difficulty_level | 체감 난이도 | 중 |

## student_error_sequence_sample.csv

| Column | Meaning | Example |
|---|---|---|
| student_id | 익명 학생 ID | S01 |
| step | 오류 발생 순서 | 1 |
| error_type | 해당 단계의 오류 유형 | Process |
| topic | 관련 단원 | 함수 |

## error_type 값

| Value | Meaning |
|---|---|
| Macro | 개념 이해 오류 |
| Micro | 계산 과정 오류 |
| Process | 문제 접근 오류 |
| Strategy | 풀이 전략 선택 오류 |

## material_preference 값

| Value | Meaning |
|---|---|
| 영상 | 짧은 설명 영상 선호 |
| 시각자료 | 그래프, 이미지, 도식 선호 |
| 예제 | 예제 중심 설명 선호 |
| 개념정리 | 개념 요약 자료 선호 |
| 문제풀이 | 문제 풀이 과정 중심 자료 선호 |
