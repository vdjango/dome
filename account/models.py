'''

Copyright (C) 2019 张珏敏.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from hanfurestful.utils import timezone





class User(AbstractUser):
    """
    用户表
    """
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    stats = models.IntegerField(choices=(
        (0, '学生'),
        (1, '教师'),
    ), default=0, help_text='当前身份')
    email = models.EmailField(_('email address'), unique=True)
    famous_race = models.CharField(help_text='名族', max_length=100, null=True, blank=True)
    native_place = models.CharField(max_length=100, help_text='籍贯', null=True, blank=True)
    age = models.IntegerField(help_text='年龄', null=True, blank=True)
    sex = models.IntegerField(help_text='性别', choices=(
        (0, '男'),
        (1, '女'),
        (2, '保密'),
    ), default=2)
    telephone = models.CharField(max_length=50, help_text='电话', null=True, blank=True)
    image = models.ImageField(help_text='头像', upload_to='', null=True, blank=True)
    id_card = models.CharField(max_length=50, help_text='身份证', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.username: self.username = timezone.mktime()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        if self.last_name: return self.last_name
        return self.username

    class Meta(AbstractUser.Meta):
        ordering = ['-id']
        pass





