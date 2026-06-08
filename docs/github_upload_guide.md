# GitHub 업로드 가이드

## 1. 웹 브라우저로 업로드하는 방법

1. GitHub에 로그인합니다.
2. 오른쪽 위 `+` 버튼을 누르고 `New repository`를 선택합니다.
3. Repository name에 `DKIS-math-mentoring-ai-toolkit`을 입력합니다.
4. 공개 여부는 선생님과 상의하여 Public 또는 Private을 선택합니다.
5. `Create repository`를 누릅니다.
6. 이 ZIP 파일을 압축 해제합니다.
7. 저장소 화면에서 `Add file` → `Upload files`를 누릅니다.
8. 압축 해제한 폴더 안의 파일과 폴더를 드래그해서 업로드합니다.
9. Commit message에 `Initial open-source toolkit upload`라고 입력합니다.
10. `Commit changes` 또는 `Propose changes` 버튼을 눌러 업로드를 완료합니다.

## 2. Git 명령어로 업로드하는 방법

```bash
git clone https://github.com/YOUR_ID/DKIS-math-mentoring-ai-toolkit.git
cd DKIS-math-mentoring-ai-toolkit
# 압축 해제한 파일들을 이 폴더 안에 복사
git add .
git commit -m "Initial open-source toolkit upload"
git push origin main
```

## 3. 주의사항

- 학생 실명이나 학번이 들어간 파일은 업로드하지 않습니다.
- 실제 원본 설문 응답은 공개하지 않습니다.
- 공개용으로는 sample CSV만 업로드합니다.
- 영상 파일이 너무 크면 GitHub 웹 업로드가 실패할 수 있습니다.
