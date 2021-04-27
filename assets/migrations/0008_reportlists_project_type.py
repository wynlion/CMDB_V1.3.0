# Generated by Django 3.1.3 on 2021-03-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20210322_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportlists',
            name='project_type',
            field=models.CharField(choices=[('JZJC', '基桩检测'), ('DJJC', '地基基础'), ('SDGC', '隧道工程'), ('GLYYJSZK', '公路营运技术状况'), ('HNTJGJC', '混凝土结构检测'), ('LJLMGC', '路基路面工程'), ('QLJG', '桥梁结构'), ('GCJCYCL', '工程监测与测量'), ('JTAQSS', '交通安全设施'), ('ZHXJC', '综合性检测'), ('ZXBG', '咨询报告')], default='', max_length=64, verbose_name='报告类型'),
        ),
    ]