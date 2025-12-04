#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class yonghu(BaseModel):
    __doc__ = u'''yonghu'''
    __tablename__ = 'yonghu'

    __loginUser__='zhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='账号' )
    xingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='姓名' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    lianxidianhua=models.CharField ( max_length=255, null=True, unique=False, verbose_name='联系电话' )
    touxiang=models.TextField   (  null=True, unique=False, verbose_name='头像' )
    '''
    zhanghao=VARCHAR
    xingming=VARCHAR
    mima=VARCHAR
    xingbie=VARCHAR
    lianxidianhua=VARCHAR
    touxiang=Text
    '''
    class Meta:
        db_table = 'yonghu'
        verbose_name = verbose_name_plural = '用户'
class jdcommentdata(BaseModel):
    __doc__ = u'''jdcommentdata'''
    __tablename__ = 'jdcommentdata'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    commentid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='评论ID' )
    productid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品ID' )
    skuid=models.CharField ( max_length=255, null=True, unique=False, verbose_name='SKUID' )
    industry=models.CharField ( max_length=255, null=True, unique=False, verbose_name='行业' )
    brand=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    productseries=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商品系列' )
    model=models.CharField ( max_length=255, null=True, unique=False, verbose_name='型号' )
    skuattribute=models.CharField ( max_length=255, null=True, unique=False, verbose_name='SKU属性' )
    userinformation=models.CharField ( max_length=255, null=True, unique=False, verbose_name='用户信息' )
    evaluationcontent=models.TextField   (  null=True, unique=False, verbose_name='评价内容' )
    ratingdetails=models.CharField ( max_length=255, null=True, unique=False, verbose_name='评分明细' )
    client=models.CharField ( max_length=255, null=True, unique=False, verbose_name='客户端' )
    evaluationtime=models.DateTimeField  (  null=True, unique=False, verbose_name='评价时间' )
    merchantresponse=models.CharField ( max_length=255, null=True, unique=False, verbose_name='商家回复' )
    commentswithpictures=models.CharField ( max_length=255, null=True, unique=False, verbose_name='带图评论' )
    followupreviewcontent=models.CharField ( max_length=255, null=True, unique=False, verbose_name='追评内容' )
    reviewtime=models.CharField ( max_length=255, null=True, unique=False, verbose_name='追评时间' )
    '''
    commentid=VARCHAR
    productid=VARCHAR
    skuid=VARCHAR
    industry=VARCHAR
    brand=VARCHAR
    productseries=VARCHAR
    model=VARCHAR
    skuattribute=VARCHAR
    userinformation=VARCHAR
    evaluationcontent=Text
    ratingdetails=VARCHAR
    client=VARCHAR
    evaluationtime=DateTime
    merchantresponse=VARCHAR
    commentswithpictures=VARCHAR
    followupreviewcontent=VARCHAR
    reviewtime=VARCHAR
    '''
    class Meta:
        db_table = 'jdcommentdata'
        verbose_name = verbose_name_plural = '京东评论数据'
class jdcommentdataforecast(BaseModel):
    __doc__ = u'''jdcommentdataforecast'''
    __tablename__ = 'jdcommentdataforecast'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    evaluationtime=models.DateTimeField  (  null=True, unique=False, verbose_name='评价时间' )
    industry=models.CharField ( max_length=255, null=True, unique=False, verbose_name='行业' )
    brand=models.CharField ( max_length=255, null=True, unique=False, verbose_name='品牌' )
    model=models.CharField ( max_length=255, null=True, unique=False, verbose_name='型号' )
    skuattribute=models.CharField ( max_length=255, null=True, unique=False, verbose_name='SKU属性' )
    ratingdetails=models.CharField ( max_length=255, null=True, unique=False, verbose_name='评分明细' )
    '''
    evaluationtime=DateTime
    industry=VARCHAR
    brand=VARCHAR
    model=VARCHAR
    skuattribute=VARCHAR
    ratingdetails=VARCHAR
    '''
    class Meta:
        db_table = 'jdcommentdataforecast'
        verbose_name = verbose_name_plural = '评分预测'
class syslog(BaseModel):
    __doc__ = u'''syslog'''
    __tablename__ = 'syslog'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    username=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户名' )
    operation=models.CharField ( max_length=255,null=False, unique=False, verbose_name='用户操作' )
    method=models.CharField ( max_length=255, null=True, unique=False, verbose_name='请求方法' )
    params=models.TextField   (  null=True, unique=False, verbose_name='请求参数' )
    time=models.BigIntegerField  (  null=True, unique=False, verbose_name='请求时长(毫秒)' )
    ip=models.CharField ( max_length=255, null=True, unique=False, verbose_name='IP地址' )
    '''
    username=VARCHAR
    operation=VARCHAR
    method=VARCHAR
    params=Text
    time=BigInteger
    ip=VARCHAR
    '''
    class Meta:
        db_table = 'syslog'
        verbose_name = verbose_name_plural = '系统日志'
