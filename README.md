# Wi-Fi Crowd Density (RSSI-based)

Raspberry Pi 기반 Wi-Fi RSSI 수집 및 분석 코드입니다.  
실험 결과나 데이터는 공개하지 않고, 코드와 문서만 업로드합니다.

## 구성
- RSSI 수집 코드: RSSI를 주기적으로 측정하고 CSV로 저장
- 분석 코드: 평균, 분산, 이동평균 계산 및 시각화
- 학습 코드: 요약 특징으로 분류 모델 학습
- 실시간 추론 코드: 최근 RSSI 데이터를 기반으로 밀집도 예측

## 설치
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt

## 사용
- RSSI 수집: 라즈베리파이에서 실행
- 분석: 수집된 CSV 파일 분석
- 학습: 통계 특징을 이용해 모델 학습
