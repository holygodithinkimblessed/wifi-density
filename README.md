# Wi-Fi Crowd Density (RSSI-based)

Raspberry Pi 기반 Wi-Fi RSSI 수집 및 분석 코드

## 구성
- RSSI 수집 코드: RSSI를 주기적으로 측정하고 CSV로 저장
- 분석 코드: 평균, 분산, 이동평균 계산 및 시각화
- 학습 코드: 요약 특징으로 분류 모델 학습
- 실시간 추론 코드: 최근 RSSI 데이터를 기반으로 밀집도 예측
