from django.db import models

# Create your models here.


"""客户端上传客户端号和分数(注意：并不会上传排名,客户端无法上传排名),同一个客户端可以多次上传分数，取最新的一次分数"""



class customer(models.Model):
    """
    同一个客户端可以多次上传分数
    """
    uid = models.IntegerField(help_text='客户端端号', unique=True)

class ranking(models.Model):
    """客户端查询排行榜"""
    number = models.IntegerField(help_text='客户端上传的分数')
    key = models.ForeignKey(customer, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-number']


class update(models.Model):
    """
    客户端上传的分数
    """
    number = models.IntegerField(help_text='同一个客户端可以多次上传分数')
    key = models.ForeignKey(customer, on_delete=models.SET_NULL, null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(update, self).save()
        ranking_ = ranking.objects.filter(key=self.key.id).first()
        if ranking_:
            max_list = [self.number, ranking_.number]
            ranking_.number = max(max_list)
            ranking_.save()
        else:
            ranking(number=self.number, key=self.key).save()





