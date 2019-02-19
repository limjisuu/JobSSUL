# Generated by Django 2.1.5 on 2019-02-19 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_scrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='payment',
            field=models.CharField(choices=[('전체', '전체'), ('7500원~9000원', '7500~9000'), ('9000원~10500원', '9000~10500'), ('10500 이상', '10500원 이상')], max_length=10, verbose_name='시급'),
        ),
        migrations.AlterField(
            model_name='post',
            name='work_type',
            field=models.CharField(choices=[('전체', '전체'), ('외식/음료', '외식/음료'), ('유통/판매', '유통/판매'), ('문화/여가/생활', '문화/여가/생활'), ('서비스', '서비스'), ('사무직', '사무직'), ('고객상담/리서치/영업', '고객상담/리서치/영업'), ('생산/건설/노무', '생산/건설/노무'), ('IT/컴퓨터', 'IT/컴퓨터'), ('교육/강사', '교육/강사'), ('디자인', '디자인'), ('미디어', '미디어'), ('운전/배달', '운전/배달'), ('병원/간호/연구', '병원/간호/연구')], help_text='알바 직종을 선택해 주세요.', max_length=10, verbose_name='직종'),
        ),
    ]
