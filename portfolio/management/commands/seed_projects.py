import os
import shutil
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils.text import slugify
from django.conf import settings
from django.core.files import File

from portfolio.models import Project, ProjectImage

PROJECTS_DATA = [
    {
        "title_fa": "پلتفرم هوشمند تشخیص عیوب و اشیاء",
        "title_en": "Intelligent Defect & Object Detection Platform",
        "kind_fa": "پلتفرم بینایی ماشین / هوش مصنوعی",
        "kind_en": "Computer Vision Platform / AI",
        "desc_fa": "یک پلتفرم هوشمند بینایی ماشین برای تشخیص عیوب و شناسایی اشیاء با هوش مصنوعی که در ابتدا برای بازرسی پنل‌های خورشیدی توسعه یافته است.",
        "desc_en": "An AI-powered machine vision platform for defect detection and object recognition, initially developed for solar panel inspection.",
        "did_fa": "خط پردازش اصلی هوش مصنوعی برای ایجاد دیتاست، برچسب‌گذاری و آموزش چندین مدل را توسعه دادم.",
        "did_en": "Built the core AI pipeline for dataset creation, labeling, and multi-model training, enabling unified image analysis.",
        "tags_fa": "بینایی ماشین, YOLO, پلتفرم, هوش مصنوعی",
        "tags_en": "Computer Vision, YOLO, Platform, AI",
        "link": "https://vipatech.ir/projects/",
    },
    {
        "title_fa": "سامانه نظارت تصویری شبکه ریلی",
        "title_en": "Railway Visual Monitoring System",
        "kind_fa": "سیستم نرم‌افزاری / PyQt",
        "kind_en": "Software System / PyQt",
        "desc_fa": "سامانه مدیریت تصاویر واگن‌های قطار، شامل سه بخش نرم‌افزار داخل واگن، واسط و استیشن مرکزی برای دریافت، انتقال و آرشیو ایمن تصاویر.",
        "desc_en": "A comprehensive software system for managing and archiving train wagon images, connecting in-cabin, interface, and central station modules.",
        "did_fa": "اپلیکیشن دسکتاپ مبتنی بر PyQt و پروتکل‌های انتقال داده امن را برای پایش ریلی توسعه دادم.",
        "did_en": "Developed the PyQt-based desktop application and secure data transfer protocols for real-time railway monitoring.",
        "tags_fa": "PyQt, اپلیکیشن دسکتاپ, Python, پایش",
        "tags_en": "PyQt, Desktop App, Python, Monitoring",
        "link": "https://vipatech.ir/projects/rail-image-monitoring/",
    },
    {
        "title_fa": "سامانه نظارت ابعادی و کنترل کیفی پیچ",
        "title_en": "Screw Dimensional Inspection System",
        "kind_fa": "بینایی صنعتی / خودکارسازی",
        "kind_en": "Industrial Vision / Automation",
        "desc_fa": "سامانه بینایی ماشین برای کنترل ابعادی و کیفی پیچ‌های صنعتی در خط تولید کارخانه یزدپیچ.",
        "desc_en": "A machine vision system for dimensional and qualitative control of industrial screws in the Yazd Pitch factory production line.",
        "did_fa": "دو دوربین صنعتی را یکپارچه کردم و الگوریتم‌های پردازش تصویر برای اندازه‌گیری و ارسال فرمان به PLC از طریق OPC توسعه دادم.",
        "did_en": "Integrated dual industrial cameras and developed image processing algorithms to measure dimensions and send reject commands via PLC OPC.",
        "tags_fa": "OpenCV, بینایی صنعتی, PLC, Python",
        "tags_en": "OpenCV, Industrial Vision, PLC, Python",
        "link": "https://vipatech.ir/projects/screw-inspection-system/",
    },
    {
        "title_fa": "دستیار هوشمند صنعت نساجی",
        "title_en": "Textile Industry Intelligent Assistant",
        "kind_fa": "دستیار هوش مصنوعی / LLM",
        "kind_en": "AI Assistant / LLM",
        "desc_fa": "دستیار هوشمند ویژه صنعت نساجی که کاربران می‌توانند به صورت متنی یا صوتی درباره فرآیندهای تولید و کنترل کیفیت با آن تعامل کنند.",
        "desc_en": "An intelligent assistant for the textile industry, allowing users to interact via text or voice regarding production processes and quality control.",
        "did_fa": "چت‌بات هوش مصنوعی را با استفاده از OpenAI API و ادغام تبدیل گفتار به متن توسعه دادم.",
        "did_en": "Developed the AI chatbot using OpenAI API, integrating speech-to-text and domain-specific knowledge retrieval.",
        "tags_fa": "LLM, OpenAI, چت‌بات, پردازش زبان طبیعی",
        "tags_en": "LLM, OpenAI, Chatbot, NLP",
        "link": "https://vipatech.ir/projects/textile-intelligent-assistant/",
    },
    {
        "title_fa": "سیستم CRM / ERP",
        "title_en": "CRM / ERP System",
        "kind_fa": "نرم‌افزار سازمانی / Django",
        "kind_en": "Enterprise Software / Django",
        "desc_fa": "یک راهکار یکپارچه سازمانی برای بهینه‌سازی گردش‌کارها، خودکارسازی مدیریت سفارش، انبار، مالی و حسابداری.",
        "desc_en": "An integrated enterprise solution to optimize organizational workflows, automating order management, inventory, finance, and accounting.",
        "did_fa": "بک‌اند کامل را با Python، Django و PostgreSQL توسعه دادم، با تضمین امنیت، مقیاس‌پذیری و تحلیل داده‌های آنی.",
        "did_en": "Developed the full back-end using Python, Django, and PostgreSQL, ensuring security, scalability, and real-time data analysis.",
        "tags_fa": "Django, PostgreSQL, ERP, بک‌اند",
        "tags_en": "Django, PostgreSQL, ERP, Back-End",
        "link": "",
    },
    {
        "title_fa": "سامانه شمارش لارو آبزیان",
        "title_en": "Aquatic Larvae Counting System",
        "kind_fa": "بینایی ماشین / موبایل",
        "kind_en": "Computer Vision / Mobile",
        "desc_fa": "سامانه‌ای مبتنی بر پردازش تصویر که با استفاده از دوربین گوشی، تعداد لاروهای آبزی را با دقت بالا و خودکار شمارش می‌کند.",
        "desc_en": "An image processing-based system that uses a smartphone camera to automatically count aquatic larvae with high accuracy.",
        "did_fa": "الگوریتم‌های پردازش تصویر و رابط کاربری موبایل‌پسند را برای شمارش در زمان واقعی توسعه دادم.",
        "did_en": "Developed the image processing algorithms and the mobile-friendly user interface for real-time counting.",
        "tags_fa": "پردازش تصویر, OpenCV, رابط موبایل",
        "tags_en": "Image Processing, OpenCV, Mobile UI",
        "link": "https://vipatech.ir/projects/",
    },
    {
        "title_fa": "بازرسی عیوب سطح ورق فولادی",
        "title_en": "Steel Sheet Surface Defect Inspection",
        "kind_fa": "هوش مصنوعی صنعتی / زمان واقعی",
        "kind_en": "Industrial AI / Real-time",
        "desc_fa": "بزرگ‌ترین پروژه هوش مصنوعی صنعتی ایران، بازرسی سطح فولاد در زمان واقعی با ۲۴ دوربین صنعتی و سرعت ۲۴۰ فریم بر ثانیه.",
        "desc_en": "The largest industrial AI project in Iran, inspecting steel surfaces in real-time using 24 industrial cameras at 240 fps.",
        "did_fa": "خط پردازش بینایی هوش مصنوعی پرسرعت را پیاده‌سازی کردم و هشدارهای عیب را به صورت آنی به اپراتورها رساندم.",
        "did_en": "Implemented the high-speed AI vision pipeline, handling multi-threading and real-time defect alerts for operators.",
        "tags_fa": "YOLO, زمان واقعی, پرسرعت, صنعتی",
        "tags_en": "YOLO, Real-time, High-speed, Industrial",
        "link": "",
    },
    {
        "title_fa": "سیستم درجه‌بندی پالت فولادی (آلمان)",
        "title_en": "German Palletcar Grading System",
        "kind_fa": "پایش هوشمند / ترکیب سنسور",
        "kind_en": "Smart Monitoring / Sensor Fusion",
        "desc_fa": "یک پروژه صنعتی با تمرکز بر پایش هوشمند و خودکارسازی، اتصال دوربین‌ها و سنسورها برای تشخیص پالت‌های فولادی و اندازه‌گیری فاصله‌ها.",
        "desc_en": "An industrial project focused on smart monitoring and automation, connecting cameras and sensors to detect steel pallets and measure distances.",
        "did_fa": "بینایی مبتنی بر هوش مصنوعی و ترکیب سنسور را برای پایش حرکت و پایداری ساختاری با هشدارهای آنی به کار گرفتم.",
        "did_en": "Applied AI-based vision and sensor fusion to monitor movement and structural stability, providing real-time alerts.",
        "tags_fa": "ترکیب سنسور, بینایی هوش مصنوعی, خودکارسازی",
        "tags_en": "Sensor Fusion, AI Vision, Automation",
        "link": "",
    },
]


class Command(BaseCommand):
    help = 'Seeds the database with project data and imports images from static folder'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Starting to seed projects...'))
        
        created_count = 0
        updated_count = 0

        # مسیر پوشه استاتیک اصلی
        base_static_dir = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'projects')

        with transaction.atomic():
            for data in PROJECTS_DATA:
                base_slug = slugify(data["title_en"])
                slug = base_slug
                counter = 1
                
                while Project.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1

                # 1. ایجاد یا به‌روزرسانی پروژه در دیتابیس
                project, created = Project.objects.update_or_create(
                    title_en=data["title_en"],
                    defaults={
                        "slug": slug,
                        "title_fa": data["title_fa"],
                        "kind_fa": data["kind_fa"],
                        "kind_en": data["kind_en"],
                        "desc_fa": data["desc_fa"],
                        "desc_en": data["desc_en"],
                        "did_fa": data["did_fa"],
                        "did_en": data["did_en"],
                        "link": data["link"],
                        "published": True,
                        "tags_fa": data["tags_fa"],
                        "tags_en": data["tags_en"],
                    }
                )

                # 2. بررسی پوشه تصاویر در static
                project_static_dir = os.path.join(base_static_dir, slug)
                
                if os.path.exists(project_static_dir):
                    # پیدا کردن تمام فایل‌های jpg و مرتب‌سازی
                    files = [f for f in os.listdir(project_static_dir) if f.lower().endswith('.jpg')]
                    files.sort(key=lambda x: int(x.split('.')[0]) if x.split('.')[0].isdigit() else 999)

                    if files:
                        self.stdout.write(f'  📸 Found {len(files)} images for "{slug}"')
                        
                        # پاک کردن عکس‌های قبلی این پروژه در دیتابیس برای جلوگیری از تکرار
                        ProjectImage.objects.filter(project=project).delete()

                        for index, filename in enumerate(files):
                            file_path = os.path.join(project_static_dir, filename)
                            
                            # باز کردن فایل و ذخیره در دیتابیس
                            with open(file_path, 'rb') as f:
                                django_file = File(f)
                                
                                # ساخت رکورد عکس جدید
                                img_obj = ProjectImage(
                                    project=project,
                                    order=index,
                                )
                                # ذخیره فایل در ImageField (جنگو خودش فایل را به MEDIA_ROOT کپی می‌کند)
                                img_obj.image.save(filename, django_file, save=True)

                                # اگر عکس اول است، آن را به عنوان کاور اصلی پروژه تنظیم کن
                                if index == 0:
                                    project.image = img_obj.image
                                    project.save()

                        self.stdout.write(self.style.SUCCESS(f'  ✅ Images imported for "{slug}"'))
                    else:
                        self.stdout.write(f'  ⚠️ Folder exists but no .jpg files in "{slug}"')
                else:
                    self.stdout.write(f'  ℹ️ No static folder for "{slug}" , {project_static_dir} (skipped images)')
                    try:
                        os.makedirs(project_static_dir)
                        self.stdout.write(f' Path created ')
                    except:
                        pass

                if created:
                    created_count += 1
                else:
                    updated_count += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {created_count} projects created, {updated_count} updated.'
        ))