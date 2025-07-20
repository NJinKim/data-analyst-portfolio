import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 시드 설정으로 재현 가능한 데이터 생성
np.random.seed(42)
random.seed(42)

def generate_tableau_data():
    """주거 관리 서비스용 더미 데이터 생성"""
    
    # 1. 공고 등록 유저 정보 생성
    def create_users(n=242):
        """공고 등록 유저 데이터 생성"""
        users_data = []
        
        for i in range(n):
            # 유저 나이 (20-70세)
            age = np.random.randint(20, 71)
            
            # 성별
            gender = np.random.choice(['남', '여'])
            
            # 동거인 수 (1-5명)
            household_size = np.random.randint(1, 6)
            
            users_data.append({
                'user_id': i + 1,
                'age': age,
                'gender': gender,
                'household_size': household_size
            })
        
        return pd.DataFrame(users_data)
    
    # 2. 주거 관리 서비스 공고 정보 생성
    def create_jobs(users_df, n=931):
        """주거 관리 서비스 공고 데이터 생성"""
        jobs_data = []
        
        # 공고 카테고리별 개수 설정 (빌라 > 아파트 > 단독주택, 차이 30 이상)
        # 총 931개: 빌라 423개, 아파트 317개, 단독주택 191개
        category_counts = {
            '빌라': 423,
            '아파트': 317,
            '단독주택': 191
        }
        
        # 주거 형태
        housing_types = ['임대', '본인 소유']
        
        # 시작일과 종료일 설정
        start_date = datetime(2025, 1, 1)
        end_date = datetime(2025, 6, 30)
        
        # 서울시 지역만 포함 (25개 구)
        korean_cities = [
            ('서울특별시', '강남구', 37.5665, 126.9780),
            ('서울특별시', '서초구', 37.4837, 127.0324),
            ('서울특별시', '마포구', 37.5519, 126.9082),
            ('서울특별시', '강서구', 37.5507, 126.8495),
            ('서울특별시', '송파구', 37.5145, 127.1059),
            ('서울특별시', '영등포구', 37.5264, 126.8962),
            ('서울특별시', '광진구', 37.5384, 127.0822),
            ('서울특별시', '성동구', 37.5506, 127.0409),
            ('서울특별시', '용산구', 37.5384, 126.9654),
            ('서울특별시', '중구', 37.5640, 126.9979),
            ('서울특별시', '종로구', 37.5735, 126.9789),
            ('서울특별시', '중랑구', 37.6064, 127.0926),
            ('서울특별시', '동대문구', 37.5744, 127.0395),
            ('서울특별시', '성북구', 37.5894, 127.0167),
            ('서울특별시', '노원구', 37.6542, 127.0568),
            ('서울특별시', '도봉구', 37.6688, 127.0471),
            ('서울특별시', '강북구', 37.6396, 127.0257),
            ('서울특별시', '은평구', 37.6027, 126.9291),
            ('서울특별시', '구로구', 37.4954, 126.8874),
            ('서울특별시', '금천구', 37.4569, 126.8956),
            ('서울특별시', '동작구', 37.5124, 126.9393),
            ('서울특별시', '관악구', 37.4784, 126.9516)
        ]
        
        # 정규분포로 유저별 공고 수 생성
        user_ids = users_df['user_id'].values
        n_users = len(user_ids)
        
        # 정규분포 기반으로 유저별 공고 수 할당 (평균 5.3개, 표준편차 2.0)
        user_post_counts = np.random.normal(5.3, 2.0, n_users)
        user_post_counts = np.maximum(user_post_counts, 1).astype(int)  # 최소 1개
        
        # 총 공고 수가 목표치에 맞도록 조정
        total_posts = sum(user_post_counts)
        if total_posts != n:
            # 부족하거나 초과하는 경우 조정
            if total_posts < n:
                # 부족한 경우 일부 유저에게 추가
                shortage = n - total_posts
                for i in range(shortage):
                    user_idx = np.random.randint(0, n_users)
                    user_post_counts[user_idx] += 1
            else:
                # 초과하는 경우 일부 유저에서 감소
                excess = total_posts - n
                for i in range(excess):
                    user_idx = np.random.randint(0, n_users)
                    if user_post_counts[user_idx] > 1:
                        user_post_counts[user_idx] -= 1
        
        job_id = 1
        
        # 각 카테고리별로 공고 생성
        for category, count in category_counts.items():
            for i in range(count):
                # 정규분포 기반으로 유저 선택
                available_users = [uid for uid, count in zip(user_ids, user_post_counts) if count > 0]
                if not available_users:
                    break
                    
                user_id = np.random.choice(available_users)
                user_idx = np.where(user_ids == user_id)[0][0]
                user_post_counts[user_idx] -= 1
                
                # 한국 도시 중 랜덤 선택
                city, district, lat, lng = random.choice(korean_cities)
                
                # 주소 생성 (시/군/구 단위)
                address = f"{city} {district}"
                
                # 위도, 경도에 약간의 랜덤성 추가 (실제 위치 분포를 위해)
                lat += np.random.uniform(-0.01, 0.01)
                lng += np.random.uniform(-0.01, 0.01)
                
                # 면적 (20-100제곱미터)
                area = round(np.random.uniform(20, 100), 1)
                
                # 방 개수 (1-5개)
                rooms = np.random.randint(1, 6)
                
                # 화장실 수 (1-3개)
                bathrooms = np.random.randint(1, 4)
                
                # 주거 형태
                housing_type = np.random.choice(housing_types)
                
                # 서비스 가격 (10,000원-300,000원)
                price = np.random.randint(10000, 300001)
                
                # 등록일 (2025년 1월 1일-6월 30일)
                days_between = (end_date - start_date).days
                random_days = np.random.randint(0, days_between + 1)
                post_date = start_date + timedelta(days=random_days)
                
                jobs_data.append({
                    'job_id': job_id,
                    'user_id': user_id,
                    'category': category,
                    'area': area,
                    'rooms': rooms,
                    'bathrooms': bathrooms,
                    'housing_type': housing_type,
                    'price': price,
                    'post_date': post_date.strftime('%Y-%m-%d'),
                    'city': city,
                    'district': district,
                    'address': address,
                    'latitude': round(lat, 6),
                    'longitude': round(lng, 6)
                })
                job_id += 1
        
        return pd.DataFrame(jobs_data)
    
    # 데이터 생성 실행
    print("주거 관리 서비스 더미 데이터 생성 중...")
    
    # 1. 유저 데이터
    users_df = create_users(242)
    print(f"유저 데이터 생성 완료: {len(users_df)}개")
    
    # 2. 공고 데이터
    jobs_df = create_jobs(users_df, 931)
    print(f"공고 데이터 생성 완료: {len(jobs_df)}개")
    
    # 데이터프레임들을 딕셔너리로 반환
    dataframes = {
        'tableau_user': users_df,
        'tableau_job': jobs_df
    }
    
    return dataframes

def save_dataframes_to_csv(dataframes, output_dir='./data'):
    """데이터프레임들을 CSV 파일로 저장"""
    import os
    
    # 출력 디렉토리 생성
    os.makedirs(output_dir, exist_ok=True)
    
    # 각 데이터프레임을 CSV로 저장
    for name, df in dataframes.items():
        filename = f"{output_dir}/{name}.csv"
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"{name}.csv 저장 완료: {len(df)}개 행")
    
    print(f"\n모든 데이터가 {output_dir} 디렉토리에 저장되었습니다.")

if __name__ == "__main__":
    # 더미 데이터 생성
    dataframes = generate_tableau_data()
    
    # CSV 파일로 저장
    save_dataframes_to_csv(dataframes)
    
    # 데이터 요약 출력
    print("\n=== 데이터 요약 ===")
    for name, df in dataframes.items():
        print(f"{name}: {len(df)}개 행, {len(df.columns)}개 컬럼")
        print(f"컬럼: {list(df.columns)}")
        print("-" * 50)
    
    # 샘플 데이터 출력
    print("\n=== 샘플 데이터 ===")
    for name, df in dataframes.items():
        print(f"\n{name} 샘플:")
        print(df.head())
        print("-" * 50) 