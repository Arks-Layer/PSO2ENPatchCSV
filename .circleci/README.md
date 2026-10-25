# KO_Reboot CircleCI

`Arks-Layer/PSO2ENPatchCSV`의 `KO_Reboot` 브랜치를 검사하고 번역 작업용 결과물을 생성한다.
설정 파일은 `.circleci/config.yml`이다.

## 실행 범위

- 워크플로: `pso2-ko-reboot`
- 실행 브랜치: `KO_Reboot`만 허용
- 태그: 실행하지 않음
- 빌드 이미지: `ghcr.io/synthsy/arks-layer-buildimages:main`
- 셸: `/bin/bash -eo pipefail`. 결과물을 gzip으로 압축할 때 원본 생성 명령의 실패도 전달한다.

원본 대조와 결과물 생성에는 upstream의 `JP_Reboot`, `EN_Reboot`, 태그가 필요하다.
따라서 전체 checkout 후 Arks-Layer 저장소를 upstream으로 가져온다.
Docker 이미지는 실행 환경으로만 사용하며, 별도의 원격 Docker 엔진은 준비하지 않는다.

## 검사와 결과물

기존 `_sh` 스크립트로 중복 폴더·파일, UTF-8, 줄 끝, BOM, CSV 형식,
NPC 이름, 파일 배치, 원문과 같은 파일의 이동, 따옴표, 중복 키,
PSO2 형식, 명령어 사용과 번역률을 검사한다.

검사가 성공하면 다음 결과물을 CircleCI의 Artifacts에서 받을 수 있다.

| 파일 | 내용 |
| --- | --- |
| `coverage.txt` | JP_Reboot 대비 번역률 |
| `PSO2.po.gz` | JP·EN·KO를 대조하는 GetText PO |
| `PSO2.CSV.gz` | JP·EN·KO를 모은 통합 CSV |
| `mplog.txt` | 기존 병렬 처리 도구의 로그 |

앞선 단계가 실패하면 이후 결과물 생성은 실행하지 않는다.
이 결과물은 게임에 설치하는 패치 배포 파일과는 구분한다.

기존 `_sh/Fonts.sh`는 파일 첫 부분에서 `exit 0`으로 종료한다.
설정에 해당 단계가 있어도 실제 폰트·한글 렌더링·표시 폭을 검사한 것으로 간주하지 않는다.
길이 검사와 실제 게임 화면 확인은 별도로 진행한다.

## CircleCI 프로젝트

Arks-Layer 조직의 기존 [PSO2ENPatchCSV 프로젝트](https://app.circleci.com/pipelines/github/Arks-Layer/PSO2ENPatchCSV)를 사용한다.
개인 포크에 별도 프로젝트를 연결할 필요는 없다.

1. Arks-Layer 저장소의 `KO_Reboot`에 `.circleci/config.yml`을 반영한다.
2. 기존 GitHub 푸시 트리거가 변경된 브랜치의 설정을 읽어 실행한다.
   이 파일의 워크플로 필터는 `KO_Reboot`만 허용한다.
3. Arks-Layer 프로젝트에서 브랜치와 커밋을 확인하고 `build` 상태와 Artifacts를 확인한다.

`Config version 2 has reached end of life` 오류가 남아 있다면 실행의 커밋과
설정 소스를 확인한다. 과거 커밋의 재실행은 과거 설정을 사용하므로,
`version: 2.1`이 반영된 최신 `KO_Reboot`의 새 실행을 확인해야 한다.

## 설정 검증

저장소 루트에서 공식 CircleCI CLI로 실행한다.

```sh
circleci config validate .circleci/config.yml
git diff --check
```

설정 검증 성공은 실제 CSV 검사와 결과물 생성 성공을 보장하지 않는다.
원격 실행에서 발견한 번역 데이터 오류는 빌드 로그의 파일·키를 확인해 별도로 수정한다.
전체 파이프라인을 로컬에서 실행하려면 Linux 실행 환경과 빌드 이미지의 의존성이 필요하다.

공식 문서: [설정 문법](https://circleci.com/docs/reference/configuration-reference/),
[프로젝트 연결](https://circleci.com/docs/guides/getting-started/create-project/).
