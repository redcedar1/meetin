from django.db import models


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
    coin = models.IntegerField(default=0)  # default 값을 0으로 수정
    # 현재 참가한 방 #related_name은 room객체에서 menInfo에 접근하기 위해 사용된다.
    participate_room = models.ForeignKey('room', on_delete=models.SET_NULL, null=True, blank=True,
                                         db_column='participate_room', related_name='men_infos')
    # 방에서 선택한 여성 #마찬가지로 related_name은 womenInfo에서 meninfo에 접근하기 위해 사용
    w_crush = models.ForeignKey('womenInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='w_crush',
                                related_name="m_crush")
    # 매칭된 여성
    w_match = models.ForeignKey('womenInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='w_match',
                                related_name="m_matched")

    def __str__(self):
        return str(self.user)


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
    coin = models.IntegerField(default=0)  # default 값을 0으로 수정
    # 현재 참가한 방
    participate_room = models.ForeignKey('room', on_delete=models.SET_NULL, null=True, blank=True,
                                         db_column='participate_room', related_name='women_infos')

    # 매칭된 남성
    m_match = models.ForeignKey('menInfo', on_delete=models.SET_NULL, null=True, blank=True, db_column='m_match')

    def __str__(self):
        return str(self.user)