from django.db import models


class Service(models.Model):
    CATEGORY_CHOICES = [
        ("ndt", "آزمون‌های غیرمخرب NDT"),
        ("dt", "آزمون‌های مخرب DT"),
        ("inspection", "بازرسی فنی"),
    ]

    title = models.CharField("عنوان", max_length=200)
    short_name = models.CharField(
        "نام اختصاری",
        max_length=50,
        blank=True
    )
    category = models.CharField(
        "دسته‌بندی",
        max_length=20,
        choices=CATEGORY_CHOICES
    )
    short_description = models.CharField(
        "توضیح کوتاه",
        max_length=300,
        blank=True
    )
    description = models.TextField("توضیحات")

    image = models.ImageField(
        "تصویر",
        upload_to="services/",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        "نمایش در صفحه اصلی",
        default=False
    )

    order = models.PositiveIntegerField(
        "ترتیب نمایش",
        default=0
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "خدمت"
        verbose_name_plural = "خدمات"

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField("عنوان پروژه", max_length=200)

    client = models.CharField(
        "کارفرما",
        max_length=200,
        blank=True
    )

    location = models.CharField(
        "محل پروژه",
        max_length=200,
        blank=True
    )

    description = models.TextField(
        "شرح پروژه",
        blank=True
    )

    services = models.ManyToManyField(
        Service,
        verbose_name="خدمات انجام‌شده",
        blank=True,
        related_name="projects"
    )

    image = models.ImageField(
        "تصویر اصلی",
        upload_to="projects/",
        blank=True,
        null=True
    )

    project_date = models.DateField(
        "تاریخ پروژه",
        blank=True,
        null=True
    )

    is_featured = models.BooleanField(
        "پروژه شاخص",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-project_date", "-created_at"]
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه‌ها"

    def __str__(self):
        return self.title


class Equipment(models.Model):
    name = models.CharField(
        "نام تجهیز",
        max_length=200
    )

    model = models.CharField(
        "مدل",
        max_length=150,
        blank=True
    )

    manufacturer = models.CharField(
        "سازنده",
        max_length=150,
        blank=True
    )

    description = models.TextField(
        "توضیحات",
        blank=True
    )

    image = models.ImageField(
        "تصویر",
        upload_to="equipment/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        "ترتیب نمایش",
        default=0
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "تجهیز"
        verbose_name_plural = "تجهیزات"

    def __str__(self):
        return self.name


class Certificate(models.Model):
    title = models.CharField(
        "عنوان مدرک",
        max_length=200
    )

    issuer = models.CharField(
        "صادرکننده",
        max_length=200,
        blank=True
    )

    description = models.TextField(
        "توضیحات",
        blank=True
    )

    image = models.ImageField(
        "تصویر مدرک",
        upload_to="certificates/images/",
        blank=True,
        null=True
    )

    file = models.FileField(
        "فایل مدرک",
        upload_to="certificates/files/",
        blank=True,
        null=True
    )

    issue_date = models.DateField(
        "تاریخ صدور",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(
        "ترتیب نمایش",
        default=0
    )

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "مجوز یا مدرک"
        verbose_name_plural = "مجوزها و مدارک"

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField("نام و نام خانوادگی", max_length=150)
    company = models.CharField("نام شرکت", max_length=200, blank=True)
    phone = models.CharField("شماره تماس", max_length=30)
    email = models.EmailField("ایمیل", blank=True)
    subject = models.CharField("موضوع", max_length=200, blank=True)
    message = models.TextField("پیام")

    is_read = models.BooleanField("خوانده شده", default=False)
    created_at = models.DateTimeField("تاریخ ارسال", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"

    def __str__(self):
        return f"{self.name} - {self.phone}"
    