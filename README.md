# DKIS Math Mentoring AI Toolkit

수학 멘토링 과정에서 수집한 학생 오류 유형을 분석하고, 학생별 학습 자료를 추천하며, Manim으로 수학 개념을 시각화하는 파일럿 프로젝트입니다.

이 저장소는 완성된 상용 AI 서비스가 아니라, 학생주도 프로젝트형 봉사활동에서 만든 **오픈소스형 학습 도구 모음**입니다. 후배들이 같은 구조를 이어받아 새로운 학생 데이터와 다른 수학 단원에도 적용할 수 있도록 코드, 샘플 데이터, 문서, 시각화 예시를 정리했습니다.

## 프로젝트 핵심 흐름

```text
설문조사 및 학생 사례 수집
→ 오류 유형 분류: Macro / Micro / Process / Strategy
→ 학생별 프로필 데이터 정리
→ 규칙 기반 추천 모델
→ Random Forest Baseline 실험
→ LSTM 오류 흐름 파일럿 실험
→ Manim 함수 그래프 시각화
```

## 주요 기능

1. 학생 오류 유형 분류 체계 정리
2. 학생별 취약 단원과 오류 유형을 기반으로 한 학습 자료 추천
3. Random Forest를 활용한 Baseline 추천 모델 실험
4. LSTM을 활용한 오류 흐름 시퀀스 파일럿 실험
5. Manim을 활용한 함수 그래프 및 오류 흐름 시각화

## 폴더 구조

```text
DKIS-math-mentoring-ai-toolkit/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── requirements.txt
├── data/
│   ├── student_profile_sample.csv
│   └── student_error_sequence_sample.csv
├── notebooks/
│   └── DKIS_math_mentoring_AI_model_pilot.ipynb
├── src/
│   └── function_error_flow_scene.py
├── docs/
│   ├── onboarding_guide.md
│   ├── teacher_operation_manual.md
│   ├── data_dictionary.md
│   ├── privacy_notice.md
│   ├── error_type_guide.md
│   ├── student_case_examples.md
│   ├── recommendation_review.md
│   └── public_dataset_review.md
└── outputs/
    ├── videos/
    │   └── function_error_flow_final.mp4
    └── figures/
        ├── error_type_distribution.png
        └── weak_topic_distribution.png
```

## 빠른 실행 방법

### 1. Colab 노트북 실행

1. `notebooks/DKIS_math_mentoring_AI_model_pilot.ipynb` 파일을 Google Colab에서 엽니다.
2. `data/student_profile_sample.csv`, `data/student_error_sequence_sample.csv` 파일을 업로드합니다.
3. 노트북 셀을 위에서부터 실행합니다.
4. 추천 결과, Baseline 결과, LSTM 파일럿 결과를 확인합니다.

### 2. Manim 영상 렌더링

로컬 또는 Colab에서 Manim이 설치된 상태에서 아래 명령어를 실행합니다.

```bash
manim -qm src/function_error_flow_scene.py FunctionErrorFlowScene
```

이미 렌더링된 예시 영상은 `outputs/videos/function_error_flow_final.mp4`에서 확인할 수 있습니다.

## 오류 유형

| 오류 유형 | 의미 | 예시 |
|---|---|---|
| Macro Error | 개념 이해 오류 | 함수의 의미나 기울기의 의미를 모름 |
| Micro Error | 계산 과정 오류 | 부호 실수, 계산 실수, 식 전개 오류 |
| Process Error | 문제 접근 오류 | 문제를 보고 무엇부터 해야 할지 모름 |
| Strategy Error | 풀이 전략 선택 오류 | 어떤 공식이나 방법을 써야 할지 모름 |

## 개인정보 보호

이 저장소에는 실제 학생 이름을 포함하지 않습니다. 모든 학생은 `S01`, `S02`와 같은 익명 ID로 표시했습니다. 실제 학생 원본 응답, 이름, 학번 등 개인을 식별할 수 있는 정보는 공개하지 않습니다.

## 활용 가능성

- 후배 학생들이 새로운 설문 결과를 같은 형식의 CSV로 추가할 수 있습니다.
- 다른 수학 단원에 대한 Manim 시각화 자료를 추가할 수 있습니다.
- 실제 멘토링 후 피드백을 반영하여 추천 규칙을 개선할 수 있습니다.
- 더 많은 데이터가 쌓이면 LSTM 파일럿 실험을 확장할 수 있습니다.

## 라이선스

코드와 문서는 MIT License로 공개합니다. 단, 실제 학생 원자료는 개인정보 보호를 위해 공개 대상에서 제외합니다.
