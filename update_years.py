"""
연도 자동화 스크립트
app.py 파일의 하드코딩된 연도를 자동 연도 변수로 교체합니다.
"""

import re
import os
from datetime import datetime

# 현재 연도 계산
current_year = datetime.now().year
current_year_str = str(current_year)

# 파일 경로 (상대 경로로 수정)
base_path = os.path.dirname(os.path.abspath(__file__))
app_path = os.path.join(base_path, 'app.py')
backup_path = os.path.join(base_path, 'app_backup.py')

# 파일 읽기
if not os.path.exists(app_path):
    print(f"Error: {app_path} 파일을 찾을 수 없습니다.")
else:
    with open(app_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 백업 생성
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)

    # 교체 매핑
    replacements = {
        # 변수명 교체 (_2023, _2024, _2025 -> _prev2, _prev1, _current)
        '_2023': '_prev2',
        '_2024': '_prev1',
        '_2025': '_current',
        
        # 문자열 내 연도 교체 ('2023', '2024', '2025' -> previous_year_2_str, previous_year_1_str, current_year_str)
        "== '2023'": "== previous_year_2_str",
        "== '2024'": "== previous_year_1_str",
        "== '2025'": "== current_year_str",
        ".contains('2025": ".contains(current_year_str",
    }

    # 특별한 패턴들 교체
    # 월별 데이터 쿼리 패턴
    for month in range(1, 13):
        month_str = f"{month:02d}"
        # 여러 형식의 패턴 대응
        old_pattern1 = f"contains('2025.{month_str}.')"
        old_pattern2 = f"contains('2025.{month}.')"
        new_pattern = f"contains(current_year_str + '.{month_str}.')"
        
        content = content.replace(old_pattern1, new_pattern)
        content = content.replace(old_pattern2, new_pattern)

    # 기본 교체 수행
    for old, new in replacements.items():
        content = content.replace(old, new)

    # 파일 저장
    with open(app_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("연도 자동화가 완료되었습니다!")
    print(f"대상 파일: {app_path}")
    print(f"백업 파일: {backup_path}")
