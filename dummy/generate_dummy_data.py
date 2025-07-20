import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# 시드 설정으로 재현 가능한 데이터 생성
np.random.seed(42)
random.seed(42)

def generate_dummy_data():
    """간병 구인 서비스용 더미 데이터 생성"""
    
    # 1. 구매 유저 정보 생성
    def create_buyer_users(n=100):
        """구매 유저 데이터 생성"""
        buyer_data = []
        
        # 한국 주요 도시와 지역
        cities = [
            ('서울특별시', '강남구', '역삼동', 37.5665, 126.9780),
            ('서울특별시', '서초구', '서초동', 37.4837, 127.0324),
            ('서울특별시', '마포구', '합정동', 37.5519, 126.9082),
            ('서울특별시', '강서구', '화곡동', 37.5507, 126.8495),
            ('부산광역시', '해운대구', '우동', 35.1586, 129.1603),
            ('부산광역시', '부산진구', '부전동', 35.1795, 129.0756),
            ('대구광역시', '수성구', '범어동', 35.8581, 128.6227),
            ('인천광역시', '연수구', '연수동', 37.3222, 126.6398),
            ('광주광역시', '서구', '치평동', 35.1595, 126.8526),
            ('대전광역시', '유성구', '구성동', 36.3626, 127.3566)
        ]
        
        for i in range(n):
            # 가입일 (최근 2년 내)
            days_ago = np.random.randint(0, 730)
            join_date = datetime.now() - timedelta(days=days_ago)
            
            # 생년월일 (20-80세)
            age = np.random.randint(20, 81)
            birth_year = datetime.now().year - age
            birth_month = np.random.randint(1, 13)
            birth_day = np.random.randint(1, 29)
            birth_date = datetime(birth_year, birth_month, birth_day)
            
            # 성별
            gender = np.random.choice(['남성', '여성'])
            
            # 지역 정보
            city, district, dong, lat, lng = random.choice(cities)
            address = f"{city} {district} {dong}"
            
            # 위도, 경도에 약간의 랜덤성 추가
            lat += np.random.uniform(-0.01, 0.01)
            lng += np.random.uniform(-0.01, 0.01)
            
            buyer_data.append({
                'user_id': i + 1,
                'join_date': join_date.strftime('%Y-%m-%d %H:%M:%S'),
                'gender': gender,
                'birth_date': birth_date.strftime('%Y-%m-%d'),
                'address': address,
                'latitude': round(lat, 6),
                'longitude': round(lng, 6)
            })
        
        return pd.DataFrame(buyer_data)
    
    # 2. 판매 유저 정보 생성
    def create_seller_users(n=150):
        """판매 유저 데이터 생성"""
        seller_data = []
        
        # 한국 주요 도시와 지역 (구매자와 동일)
        cities = [
            ('서울특별시', '강남구', '역삼동', 37.5665, 126.9780),
            ('서울특별시', '서초구', '서초동', 37.4837, 127.0324),
            ('서울특별시', '마포구', '합정동', 37.5519, 126.9082),
            ('서울특별시', '강서구', '화곡동', 37.5507, 126.8495),
            ('부산광역시', '해운대구', '우동', 35.1586, 129.1603),
            ('부산광역시', '부산진구', '부전동', 35.1795, 129.0756),
            ('대구광역시', '수성구', '범어동', 35.8581, 128.6227),
            ('인천광역시', '연수구', '연수동', 37.3222, 126.6398),
            ('광주광역시', '서구', '치평동', 35.1595, 126.8526),
            ('대전광역시', '유성구', '구성동', 36.3626, 127.3566)
        ]
        
        # 자격증 종류
        certificates = ['A', 'B', 'C', 'D', 'E']
        
        for i in range(n):
            # 가입일 (최근 3년 내)
            days_ago = np.random.randint(0, 1095)
            join_date = datetime.now() - timedelta(days=days_ago)
            
            # 생년월일 (25-65세)
            age = np.random.randint(25, 66)
            birth_year = datetime.now().year - age
            birth_month = np.random.randint(1, 13)
            birth_day = np.random.randint(1, 29)
            birth_date = datetime(birth_year, birth_month, birth_day)
            
            # 성별
            gender = np.random.choice(['남성', '여성'])
            
            # 지역 정보
            city, district, dong, lat, lng = random.choice(cities)
            address = f"{city} {district} {dong}"
            
            # 위도, 경도에 약간의 랜덤성 추가
            lat += np.random.uniform(-0.01, 0.01)
            lng += np.random.uniform(-0.01, 0.01)
            
            # 경력 (0-20년)
            experience = np.random.randint(0, 21)
            
            # 자격증 (1-3개)
            num_certificates = np.random.randint(1, 4)
            user_certificates = ','.join(random.sample(certificates, num_certificates))
            
            seller_data.append({
                'user_id': i + 1,
                'join_date': join_date.strftime('%Y-%m-%d %H:%M:%S'),
                'gender': gender,
                'birth_date': birth_date.strftime('%Y-%m-%d'),
                'address': address,
                'latitude': round(lat, 6),
                'longitude': round(lng, 6),
                'experience': experience,
                'certificates': user_certificates
            })
        
        return pd.DataFrame(seller_data)
    
    # 3. 구매 공고 데이터 생성
    def create_posts(buyer_df, n=200):
        """구매 공고 데이터 생성"""
        posts_data = []
        
        # 환자 병명
        diseases = [
            '뇌졸중', '치매', '파킨슨병', '당뇨병', '고혈압', '심장질환',
            '폐질환', '관절염', '골다공증', '암', '척추질환', '신장질환'
        ]
        
        # 공고 상태
        statuses = ['등록', '지원', '매칭', '삭제', '진행 중']
        status_weights = [0.3, 0.2, 0.2, 0.1, 0.2]
        
        for i in range(n):
            # 등록한 구매 유저 ID
            buyer_id = np.random.choice(buyer_df['user_id'].values)
            
            # 공고 등록일 (최근 1년 내)
            days_ago = np.random.randint(0, 365)
            post_date = datetime.now() - timedelta(days=days_ago)
            
            # 환자 병명
            disease = np.random.choice(diseases)
            
            # 주요 증상들 (0 또는 1)
            symptoms = {
                'symptom1_mobility': np.random.choice([0, 1], p=[0.7, 0.3]),
                'symptom2_bowel': np.random.choice([0, 1], p=[0.8, 0.2]),
                'symptom3_infectious': np.random.choice([0, 1], p=[0.9, 0.1]),
                'symptom4_bedsore': np.random.choice([0, 1], p=[0.8, 0.2]),
                'symptom5_dementia': np.random.choice([0, 1], p=[0.7, 0.3]),
                'symptom6_suction': np.random.choice([0, 1], p=[0.9, 0.1])
            }
            
            # 예측 가격 (일당 기준, 5만원-15만원)
            predicted_price = np.random.randint(50000, 150001)
            
            # 공고 상태
            status = np.random.choice(statuses, p=status_weights)
            
            # 시작일, 종료일 (공고일로부터 1-30일 후 시작, 1-90일간 진행)
            start_days = np.random.randint(1, 31)
            duration_days = np.random.randint(1, 91)
            start_date = post_date + timedelta(days=start_days)
            end_date = start_date + timedelta(days=duration_days)
            
            posts_data.append({
                'post_id': i + 1,
                'post_date': post_date.strftime('%Y-%m-%d %H:%M:%S'),
                'buyer_id': buyer_id,
                'disease': disease,
                'symptom1_mobility': symptoms['symptom1_mobility'],
                'symptom2_bowel': symptoms['symptom2_bowel'],
                'symptom3_infectious': symptoms['symptom3_infectious'],
                'symptom4_bedsore': symptoms['symptom4_bedsore'],
                'symptom5_dementia': symptoms['symptom5_dementia'],
                'symptom6_suction': symptoms['symptom6_suction'],
                'predicted_price': predicted_price,
                'status': status,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d')
            })
        
        return pd.DataFrame(posts_data)
    
    # 4. 지원 데이터 생성
    def create_applications(posts_df, seller_df, n=300):
        """지원 데이터 생성"""
        applications_data = []
        
        # 매칭된 공고만 필터링
        matched_posts = posts_df[posts_df['status'].isin(['지원', '매칭', '진행 중'])]['post_id'].values
        
        for i in range(n):
            # 지원할 공고 ID
            post_id = np.random.choice(matched_posts)
            
            # 지원한 판매 유저 ID
            seller_id = np.random.choice(seller_df['user_id'].values)
            
            # 지원일 (공고 등록일 이후)
            post_date = datetime.strptime(posts_df[posts_df['post_id'] == post_id]['post_date'].iloc[0], '%Y-%m-%d %H:%M:%S')
            days_after = np.random.randint(1, 15)
            apply_date = post_date + timedelta(days=days_after)
            
            # 지원가격 (예측가격의 80-120%)
            predicted_price = posts_df[posts_df['post_id'] == post_id]['predicted_price'].iloc[0]
            apply_price = int(predicted_price * np.random.uniform(0.8, 1.2))
            
            applications_data.append({
                'application_id': i + 1,
                'post_id': post_id,
                'seller_id': seller_id,
                'apply_date': apply_date.strftime('%Y-%m-%d %H:%M:%S'),
                'apply_price': apply_price
            })
        
        return pd.DataFrame(applications_data)
    
    # 5. 매칭 데이터 생성
    def create_matches(posts_df, applications_df, n=100):
        """매칭 데이터 생성"""
        matches_data = []
        
        # 매칭된 공고만 필터링
        matched_posts = posts_df[posts_df['status'].isin(['매칭', '진행 중'])]['post_id'].values
        
        for i in range(n):
            # 매칭할 공고 ID
            post_id = np.random.choice(matched_posts)
            
            # 해당 공고에 지원한 판매자 중 선택
            post_applications = applications_df[applications_df['post_id'] == post_id]
            if len(post_applications) > 0:
                selected_application = post_applications.sample(1).iloc[0]
                seller_id = selected_application['seller_id']
                match_price = selected_application['apply_price']
            else:
                # 지원 데이터가 없는 경우 랜덤 생성
                seller_id = np.random.choice(posts_df['buyer_id'].values)  # 임시로 buyer_id 사용
                match_price = np.random.randint(50000, 150001)
            
            # 결제 상태
            payment_status = np.random.choice(['결제 전', '취소', '결제 완료'], p=[0.2, 0.1, 0.7])
            
            # 매칭일 (공고 등록일 이후)
            post_date = datetime.strptime(posts_df[posts_df['post_id'] == post_id]['post_date'].iloc[0], '%Y-%m-%d %H:%M:%S')
            days_after = np.random.randint(5, 20)
            match_date = post_date + timedelta(days=days_after)
            
            matches_data.append({
                'match_id': i + 1,
                'post_id': post_id,
                'seller_id': seller_id,
                'match_price': match_price,
                'payment_status': payment_status,
                'match_date': match_date.strftime('%Y-%m-%d %H:%M:%S')
            })
        
        return pd.DataFrame(matches_data)
    
    # 6. 서비스 진행 데이터 생성
    def create_service_progress(matches_df, posts_df, n=80):
        """서비스 진행 데이터 생성"""
        service_data = []
        
        # 결제 완료된 매칭만 필터링
        completed_matches = matches_df[matches_df['payment_status'] == '결제 완료']
        
        for i in range(n):
            if len(completed_matches) == 0:
                break
                
            # 매칭 선택
            match_row = completed_matches.sample(1).iloc[0]
            match_id = match_row['match_id']
            post_id = match_row['post_id']
            
            # 시작일자, 종료일자 (매칭일 기준)
            match_date = datetime.strptime(match_row['match_date'], '%Y-%m-%d %H:%M:%S')
            start_days = np.random.randint(1, 8)
            duration_days = np.random.randint(1, 31)
            
            start_date = match_date + timedelta(days=start_days)
            end_date = start_date + timedelta(days=duration_days)
            
            # 진행일자 (시작일과 종료일 사이)
            progress_date = start_date + timedelta(days=np.random.randint(0, duration_days))
            
            # 금액 지급 여부
            payment_made = np.random.choice([0, 1], p=[0.3, 0.7])
            
            service_data.append({
                'service_id': i + 1,
                'post_id': post_id,
                'match_id': match_id,
                'start_date': start_date.strftime('%Y-%m-%d'),
                'end_date': end_date.strftime('%Y-%m-%d'),
                'progress_date': progress_date.strftime('%Y-%m-%d'),
                'payment_made': payment_made
            })
        
        return pd.DataFrame(service_data)
    
    # 7. 서비스 평가 데이터 생성
    def create_service_reviews(service_df, n=60):
        """서비스 평가 데이터 생성"""
        reviews_data = []
        
        for i in range(n):
            if len(service_df) == 0:
                break
                
            # 서비스 선택
            service_row = service_df.sample(1).iloc[0]
            service_id = service_row['service_id']
            post_id = service_row['post_id']
            match_id = service_row['match_id']
            
            # 평점 생성 (정규분포 기반, 평균 4.0, 표준편차 0.8)
            overall_rating = max(0, min(5, np.random.normal(4.0, 0.8)))
            kindness_rating = max(0, min(5, np.random.normal(4.0, 0.8)))
            skill_rating = max(0, min(5, np.random.normal(4.0, 0.8)))
            carefulness_rating = max(0, min(5, np.random.normal(4.0, 0.8)))
            hygiene_rating = max(0, min(5, np.random.normal(4.0, 0.8)))
            
            reviews_data.append({
                'review_id': i + 1,
                'post_id': post_id,
                'match_id': match_id,
                'overall_rating': round(overall_rating, 1),
                'kindness_rating': round(kindness_rating, 1),
                'skill_rating': round(skill_rating, 1),
                'carefulness_rating': round(carefulness_rating, 1),
                'hygiene_rating': round(hygiene_rating, 1)
            })
        
        return pd.DataFrame(reviews_data)
    
    # 데이터 생성 실행
    print("더미 데이터 생성 중...")
    
    # 1. 구매 유저 데이터
    buyer_df = create_buyer_users(100)
    print(f"구매 유저 데이터 생성 완료: {len(buyer_df)}개")
    
    # 2. 판매 유저 데이터
    seller_df = create_seller_users(150)
    print(f"판매 유저 데이터 생성 완료: {len(seller_df)}개")
    
    # 3. 구매 공고 데이터
    posts_df = create_posts(buyer_df, 200)
    print(f"구매 공고 데이터 생성 완료: {len(posts_df)}개")
    
    # 4. 지원 데이터
    applications_df = create_applications(posts_df, seller_df, 300)
    print(f"지원 데이터 생성 완료: {len(applications_df)}개")
    
    # 5. 매칭 데이터
    matches_df = create_matches(posts_df, applications_df, 100)
    print(f"매칭 데이터 생성 완료: {len(matches_df)}개")
    
    # 6. 서비스 진행 데이터
    service_df = create_service_progress(matches_df, posts_df, 80)
    print(f"서비스 진행 데이터 생성 완료: {len(service_df)}개")
    
    # 7. 서비스 평가 데이터
    reviews_df = create_service_reviews(service_df, 60)
    print(f"서비스 평가 데이터 생성 완료: {len(reviews_df)}개")
    
    # 데이터프레임들을 딕셔너리로 반환
    dataframes = {
        'buyer_users': buyer_df,
        'seller_users': seller_df,
        'posts': posts_df,
        'applications': applications_df,
        'matches': matches_df,
        'service_progress': service_df,
        'service_reviews': reviews_df
    }
    
    return dataframes

def save_dataframes_to_csv(dataframes, output_dir='portfolio/dummy/data'):
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
    dataframes = generate_dummy_data()
    
    # CSV 파일로 저장
    save_dataframes_to_csv(dataframes)
    
    # 데이터 요약 출력
    print("\n=== 데이터 요약 ===")
    for name, df in dataframes.items():
        print(f"{name}: {len(df)}개 행, {len(df.columns)}개 컬럼")
        print(f"컬럼: {list(df.columns)}")
        print("-" * 50) 