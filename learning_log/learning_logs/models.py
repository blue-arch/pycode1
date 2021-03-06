from django.db import models

# Create your models here.

class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """放回模型的字符串表示"""
        return self.text

class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    # 外键是一个数据库术语， 它引用了数据库中的另一条记录； 这些代码将每个条目关联到特定的主题。 每个主题创建时， 都给它分配了一个键（或ID） 。
    # https://docs.djangoproject.com/en/2.2/ref/models/fields/#foreignkey
    # 注 在django2.0后定义外键和一对一关系的时候需要加on_delete选项
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    '''
    书中源代码：
        topic = models.ForeignKey(Topic)
    '''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    # 在Entry 类中嵌套了Meta 类。 Meta 存储用于管理模型的额外信息， 在这里， 它让我们能够设置一个特殊属性， 让Django在需要时使用Entries 来表示多个条目。
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + "..."    # 由于条目包含的文本可能很长， 我们让Django只显示text 的前50个字符


