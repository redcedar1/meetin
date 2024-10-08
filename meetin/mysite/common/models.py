from django.db import models


class Info(models.Model):
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=10, null=True, blank=True)
    peoplenum = models.TextField(max_length=10, null=True, blank=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    mbti = models.CharField(max_length=10, null=True, blank=True)
    army = models.CharField(max_length=10, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    body = models.CharField(max_length=10, null=True, blank=True)
    eyes = models.CharField(max_length=10, null=True, blank=True)
    face = models.CharField(max_length=10, null=True, blank=True)
    hobby = models.CharField(max_length=100, null=True, blank=True)
    jobs = models.CharField(max_length=100, blank=True, null=True)
    avgage = models.IntegerField(null=True, blank=True)
    ages = models.TextField(null=True, blank=True)  # 정수로 이루어진 리스트를 문자열로 저장
    kakao_id = models.CharField(max_length=100, blank=True, null=True)  # kakao_id를 기본 키로 설정
    free = models.TextField(null=True, blank=True)
    kakaotalk_id = models.CharField(max_length=20, null=True, blank=True)
    you_kakao_id = models.CharField(max_length=100, blank=True, null=True)
    matching_time = models.DateTimeField(null=True, blank=True)

    # 매칭 성사 여부 (IntegerField로 변경)
    matching_success = models.IntegerField(default=0)

    # 매칭 신청 여부
    matching_application = models.IntegerField(default=0)

    # 매칭 동의 여부
    matching_agreement = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pk)


class menInfo(models.Model):
    id = models.AutoField(primary_key=True)

    # 앱 내에서 사용할 닉네임
    nickname = models.CharField(max_length=50)

    # 자기소개 시 입력되는 내 정보
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    mbti = models.CharField(max_length=10, null=True, blank=True)
    army = models.CharField(max_length=10, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    body = models.CharField(max_length=10, null=True, blank=True)
    eyes = models.CharField(max_length=10, null=True, blank=True)
    face = models.CharField(max_length=10, null=True, blank=True)
    hobby = models.CharField(max_length=100, null=True, blank=True)
    # 참가자 평균 나이
    avgage = models.IntegerField(null=True)
    # 이상형 정보
    w_age = models.CharField(max_length=50, null=True, blank=True)
    w_job = models.CharField(max_length=50, null=True, blank=True)
    w_school = models.CharField(max_length=50, null=True, blank=True)
    w_major = models.CharField(max_length=50, null=True, blank=True)
    w_mbti = models.CharField(max_length=10, null=True, blank=True)
    w_height = models.CharField(max_length=10, null=True, blank=True)
    w_body = models.CharField(max_length=10, null=True, blank=True)
    w_eyes = models.CharField(max_length=10, null=True, blank=True)
    w_face = models.CharField(max_length=10, null=True, blank=True)
    w_hobby = models.CharField(max_length=100, null=True, blank=True)

    # 자유로운 자기소개
    free = models.TextField(null=True, blank=True)
    # 자기소개 시 입력하는 실제 카카오톡 아이디
    kakaotalk_id = models.CharField(max_length=20, null=True, blank=True)
    # 보유 코인
    coin = models.IntegerField(default=0)
    # 매칭된 여성
    w_match = models.ForeignKey('womenInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='w_match',
                                related_name="m_matched")

    def __str__(self):
        return str(self.pk)


class womenInfo(models.Model):
    id = models.AutoField(primary_key=True)
    # 앱 내에서 사용할 닉네임
    nickname = models.CharField(max_length=50)

    # 자기소개 시 입력되는 내 정보
    age = models.IntegerField(null=True)
    job = models.CharField(max_length=50, null=True, blank=True)
    school = models.CharField(max_length=50, null=True, blank=True)
    major = models.CharField(max_length=50, null=True, blank=True)
    mbti = models.CharField(max_length=10, null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    body = models.CharField(max_length=10, null=True, blank=True)
    eyes = models.CharField(max_length=10, null=True, blank=True)
    face = models.CharField(max_length=10, null=True, blank=True)
    hobby = models.CharField(max_length=100, null=True, blank=True)
    # 참가자 평균 나이
    avgage = models.IntegerField(null=True)
    # 이상형 정보
    m_age = models.CharField(max_length=50, null=True, blank=True)
    m_job = models.CharField(max_length=50, null=True, blank=True)
    m_school = models.CharField(max_length=50, null=True, blank=True)
    m_major = models.CharField(max_length=50, null=True, blank=True)
    m_mbti = models.CharField(max_length=10, null=True, blank=True)
    m_army = models.CharField(max_length=10, null=True, blank=True)
    m_height = models.CharField(max_length=10, null=True, blank=True)
    m_body = models.CharField(max_length=10, null=True, blank=True)
    m_eyes = models.CharField(max_length=10, null=True, blank=True)
    m_face = models.CharField(max_length=10, null=True, blank=True)
    m_hobby = models.CharField(max_length=100, null=True, blank=True)

    # 자유로운 자기소개
    free = models.TextField(null=True, blank=True)
    # 자기소개 시 입력하는 실제 카카오톡 아이디
    kakaotalk_id = models.CharField(max_length=20, null=True, blank=True)
    # 보유 코인
    coin = models.IntegerField(default=0)

    # 매칭된 남성
    m_match = models.ForeignKey('menInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='m_match')

    def __str__(self):
        return str(self.pk)

class matchingInfo(models.Model):
    #매칭정보의 고유번호(매칭정보의 기본키)
    matchingnum = models.CharField(max_length=10, primary_key=True)

    #매칭된 남성
    matched_man = models.ForeignKey('menInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='matched_man')
    #매칭된 여성
    matched_woman = models.ForeignKey('womenInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='matched_woman')

    def __str__(self):
        return str(self.pk)

class Location(models.Model):
    user = models.ForeignKey(Info, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.kakao_id} - {self.latitude}, {self.longitude} at {self.timestamp}"