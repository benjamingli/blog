# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
from collections import OrderedDict


# Create your models here.

def decode(info):
    return info.decode('utf-8')

class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    def __unicode__(self):
        return self.name

class ArticleManager(models.Model):
    def get_Article_onDate(self):
        post_date = Article.objects.dates('publish_time','month')
        date_list = []
        for i in range(len(post_date)):
            date_list.append([])
        for i in range(len(post_date)):
            curyear = post_date[i].year
            curmonth = post_date[i].month
            tempArticle = Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            tempNum = len(tempArticle)
            date_list[i].append(post_date[i])
            date_list[i].append(tempNum)
        return date_list
    def get_Article_OnArchive(self):
        post_date = Article.objects.dates('publish_time','month')
        post_date_article = []
        for i in range(len(post_date)):
            post_date_article.append([])

        for i in range(len(post_date)):
            curyear = post_date[i].year
            curmonth = post_date[i].month
            tempArticle = Article.objects.filter(publish_time__year=curyear).filter(publish_time__month=curmonth)
            post_date_article[i] = tempArticle

        dicts=OrderedDict()
        for i in range(len(post_date)):
            dicts.setdefault(post_date[i],post_date_article[i])
        return dicts

class Article(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author)
    content = models.TextField(blank=True,null=True)
    publish_time = models.DateTimeField(auto_now_add=True)


    objects = models.Manager()
    date_list = ArticleManager()
    
    @models.permalink
    def get_absolute_url(self):
        return('detail',(),{
            'id':self.id,
            'month':self.publish_time.strftime('%m'),
            'day':self.publish_time.strftime('%d'),
            'year':self.publish_time.year,})

    def get_before_article(self):
        temp = Article.objects.order_by('id')
        cur = Article.objects.get(id=self.id)
        count = 0
        for i in temp:
            if i.id == cur.id:
                index = count
                break
            else:
                count+=1
        if index != 0:
            return temp[index-1]

    def get_after_article(self):
        temp = Article.objects.order_by('id')
        max = len(temp)-1
        cur = Article.objects.get(id=self.id)
        count = 0 
        for i in temp:
            if i.id == cur.id:
                index = count
                break
            else:
                count+=1
        if index != max:
            return temp[index+1]


    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ['-publish_time']
