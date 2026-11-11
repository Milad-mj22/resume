"""
تمام متن‌های سایت اینجاست. برای تغییر اسم، پروژه‌ها، نظرات و ... فقط همین فایل را ویرایش کنید.
"""

DEFAULT_LANG = "fa"

# At the top of portfolio/content.py, after DEFAULT_LANG
DEFAULT_THEME = "ocean"

THEMES = [
    {"key": "ocean",  "label_en": "Ocean",  "label_fa": "اقیانوس",  "color": "#3b82f6"},
    {"key": "forest", "label_en": "Forest", "label_fa": "جنگل",     "color": "#22c55e"},
    {"key": "violet", "label_en": "Violet", "label_fa": "بنفش",     "color": "#8b5cf6"},
    {"key": "rose",   "label_en": "Rose",   "label_fa": "رز",       "color": "#ec4899"},
    {"key": "gold",   "label_en": "Gold",   "label_fa": "طلایی",    "color": "#eab308"},
]



CONTENT = {
    # ------------------------------------------------------------------ English
    "en": {
        "name": "Milad Moltaji",
        "brand": "Milad Moltaji",
        "title": "Milad Moltaji — Software & AI Developer",
        "lang_label": "English",
        "flag": "🇺🇸",
        "nav": [
            ("about", "About"),
            ("skills", "Skills"),
            ("work", "Selected work"),
            ("reviews", "Reviews"),
            ("blog", "Blog"),
            ("experience", "Experience"),      # در en
            ("certificates", "Certificates"),
        ],
        "cta": "Get in touch",
        "hero": {
            "eyebrow": "Portfolio",
            "hey": "Hey, I'm a",
            "line1": "",
            "line2": "Software & AI Developer",
            "text": "I build reliable software and AI-powered solutions — from desktop apps with PyQt to computer-vision models with YOLO and LLM-based systems — and help businesses automate and smarten up their operations.",
            "link": "Explore my projects",
        },
        "stats": [
            ("6", "Years of experience"),
            ("15", "Projects shipped"),
            ("15", "Happy clients"),
            ("95", "Client satisfaction"),
        ],
        "about": {
            "eyebrow": "Behind the work",
            "title_a": "Building software.",
            "title_b": "Making it intelligent.",
            "lead": "I'm a software and AI developer turning ambitious ideas into scalable, intelligent systems.",
            "text": "From architecture and APIs to AI models and automation pipelines, I care about every detail: reliability, performance, and how smoothly it works for the business behind it. My toolkit spans back-end frameworks like Django and FastAPI, desktop apps with PyQt, computer vision with YOLO and OpenCV, and LLM-powered assistants.",
            "cta": "Get in touch",
        },
        "experience": {"eyebrow": "Experience", "title": "Where I've worked"}, 
        "certificates": {"eyebrow": "Certificates", "title": "Certifications & awards"}, 
        "skills_title": "Tools I reach for",
        "skills": [
            ("Python / Django", 100), ("FastAPI", 95), ("REST & APIs", 90),
            ("PostgreSQL / MySQL", 85), ("Redis / Celery", 80),
            ("AI & Machine Learning", 90), ("PyTorch / TensorFlow", 80),
            ("LLM / RAG / OpenAI API", 85), ("Computer Vision / YOLO", 90),
            ("OpenCV", 85), ("React", 85), ("TypeScript", 80),
            ("PyQt", 95), ("Docker", 85), ("Git / GitHub", 90),
            ("Linux / CLI", 85), ("CI/CD", 80), ("Testing (Pytest)", 85),
        ],
        "work": {
            "eyebrow": "Selected work",
            "title": "Projects I'm proud of",
            "label": "What I did",
        },
        "projects": [
            {
                "title": "Intelligent Defect & Object Detection Platform",
                "kind": "Computer Vision Platform / AI",
                "desc": "An AI-powered machine vision platform for defect detection and object recognition, initially developed for solar panel inspection.",
                "did": "Built the core AI pipeline for dataset creation, labeling, and multi-model training, enabling unified image analysis.",
                "tags": ["Computer Vision", "YOLO", "Platform", "AI"],
                "link": "https://vipatech.ir/projects/",
            },
            {
                "title": "Railway Visual Monitoring System",
                "kind": "Software System / PyQt",
                "desc": "A comprehensive software system for managing and archiving train wagon images, connecting in-cabin, interface, and central station modules.",
                "did": "Developed the PyQt-based desktop application and secure data transfer protocols for real-time railway monitoring.",
                "tags": ["PyQt", "Desktop App", "Python", "Monitoring"],
                "link": "https://vipatech.ir/projects/rail-image-monitoring/",
            },
            {
                "title": "Screw Dimensional Inspection System",
                "kind": "Industrial Vision / Automation",
                "desc": "A machine vision system for dimensional and qualitative control of industrial screws in the Yazd Pitch factory production line.",
                "did": "Integrated dual industrial cameras and developed image processing algorithms to measure dimensions and send reject commands via PLC OPC.",
                "tags": ["OpenCV", "Industrial Vision", "PLC", "Python"],
                "link": "https://vipatech.ir/projects/screw-inspection-system/",
            },
            {
                "title": "Textile Industry Intelligent Assistant",
                "kind": "AI Assistant / LLM",
                "desc": "An intelligent assistant for the textile industry, allowing users to interact via text or voice regarding production processes and quality control.",
                "did": "Developed the AI chatbot using OpenAI API, integrating speech-to-text and domain-specific knowledge retrieval.",
                "tags": ["LLM", "OpenAI", "Chatbot", "NLP"],
                "link": "https://vipatech.ir/projects/textile-intelligent-assistant/",
            },
            {
                "title": "CRM / ERP System",
                "kind": "Enterprise Software / Django",
                "desc": "An integrated enterprise solution to optimize organizational workflows, automating order management, inventory, finance, and accounting.",
                "did": "Developed the full back-end using Python, Django, and PostgreSQL, ensuring security, scalability, and real-time data analysis.",
                "tags": ["Django", "PostgreSQL", "ERP", "Back-End"],
                "link": "#",
            },
            {
                "title": "Aquatic Larvae Counting System",
                "kind": "Computer Vision / Mobile",
                "desc": "An image processing-based system that uses a smartphone camera to automatically count aquatic larvae with high accuracy.",
                "did": "Developed the image processing algorithms and the mobile-friendly user interface for real-time counting.",
                "tags": ["Image Processing", "OpenCV", "Mobile UI"],
                "link": "https://vipatech.ir/projects/",
            },
            {
                "title": "Steel Sheet Surface Defect Inspection",
                "kind": "Industrial AI / Real-time",
                "desc": "The largest industrial AI project in Iran, inspecting steel surfaces in real-time using 24 industrial cameras at 240 fps.",
                "did": "Implemented the high-speed AI vision pipeline, handling multi-threading and real-time defect alerts for operators.",
                "tags": ["YOLO", "Real-time", "High-speed", "Industrial"],
                "link": "#",
            },
            {
                "title": "German Palletcar Grading System",
                "kind": "Smart Monitoring / Sensor Fusion",
                "desc": "An industrial project focused on smart monitoring and automation, connecting cameras and sensors to detect steel pallets and measure distances.",
                "did": "Applied AI-based vision and sensor fusion to monitor movement and structural stability, providing real-time alerts.",
                "tags": ["Sensor Fusion", "AI Vision", "Automation"],
                "link": "#",
            },
        ],
        "reviews": {
            "eyebrow": "Colleague & client reviews",
            "title": "Better work happens together.",
            "items": [
                {"text": "The rare kind of developer who makes an ambitious system feel effortless to use. Every decision felt intentional, and the result was as reliable as it was fast.", "name": "Sara Karimi", "role": "Product Designer"},
                {"text": "Communicates clearly, delivers on time and cares about the details nobody asked for.", "name": "Reza Ahmadi", "role": "Project Manager"},
                {"text": "He turned our rough requirements into a polished, fast software solution in two weeks.", "name": "Nima Rahimi", "role": "Startup Founder"},
                {"text": "Clean code, thoughtful decisions and zero drama. I'd work with him again.", "name": "Mina Hosseini", "role": "Front-End Developer"},
            ],
        },
        "contact": {
            "eyebrow": "Good work starts with a conversation",
            "title": "Ready to build?",
            "text": "Tell me about your project and I'll get back to you within a day.",
            "name": "Your name", "phone": "Your number", "email": "Your email",
            "project": "What do you want to build?", "message": "Message",
            "project_options": [
                "Software system", "AI solution", "Computer vision / YOLO",
                "Desktop app (PyQt)", "Business automation", "API / integration", "Something else"
            ],
            "submit": "Send message",
            "sending": "Sending…",
            "success": "Thanks! Your message was sent.",
            "error": "Something went wrong. Check the fields and try again.",
        },
        "footer": "© 2026 Milad Moltaji. All rights reserved.",
        "ui": {
            "blog": "Blog", "blog_eyebrow": "Writing", "blog_title": "Notes on building software & AI",
            "blog_text": "Short articles about software engineering, AI, automation and what I learn along the way.",
            "blog_empty": "No posts yet. Add one from the admin panel.", "read_more": "Read article",
            "back_blog": "All articles", "back_work": "All projects", "visit": "Visit project",
            "overview": "Overview", "more_work": "More projects", "latest": "From the blog",
            "all_posts": "View all articles",
            "all_projects": "View all projects",
            "pdf": "PDF",
        },
    },

    # ------------------------------------------------------------------ Persian
    "fa": {
        "name": "میلاد ملتجی",
        "brand": "میلاد ملتجی",
        "title": "میلاد ملتجی — توسعه‌دهنده نرم‌افزار و هوش مصنوعی",
        "lang_label": "فارسی",
        "flag": "🇮🇷",
        "nav": [
            ("about", "درباره"),
            ("skills", "مهارت‌ها"),
            ("work", "نمونه‌کارها"),
            ("reviews", "نظرها"),
            ("blog", "وبلاگ"),
            ("experience", "سابقه کاری"),      # در fa
            ("certificates", "گواهینامه‌ها"),
        ],
        "cta": "ارتباط با من",
        "hero": {
            "eyebrow": "پورتفولیو",
            "hey": "سلام، من یک",
            "line1": "",
            "line2": "توسعه‌دهنده نرم‌افزار و هوش مصنوعی هستم",
            "text": "نرم‌افزارهای قابل‌اعتماد و راهکارهای مبتنی بر هوش مصنوعی می‌سازم — از اپلیکیشن‌های دسکتاپ با PyQt تا مدل‌های بینایی ماشین با YOLO و سیستم‌های مبتنی بر LLM — و به کسب‌وکارها کمک می‌کنم فرایندهایشان را هوشمند و خودکار کنند.",
            "link": "پروژه‌هایم را ببینید",
        },
        "stats": [
            ("۶", "سال تجربه"),
            ("۱۵", "پروژه تحویل‌شده"),
            ("۱۵", "کارفرمای راضی"),
            ("۹۵", "رضایت کارفرما"),
        ],
        "about": {
            "eyebrow": "پشت صحنه کار",
            "title_a": "ساختن نرم‌افزارهایی",
            "title_b": "که هوشمند کار می‌کنند.",
            "lead": "توسعه‌دهنده نرم‌افزار و هوش مصنوعی که ایده‌های جاه‌طلبانه را به سیستم‌های مقیاس‌پذیر و هوشمند تبدیل می‌کند.",
            "text": "از معماری و API تا مدل‌های هوش مصنوعی و خطوط خودکارسازی، به همه جزئیات اهمیت می‌دهم: پایداری، کارایی و روان‌بودن آن برای کسب‌وکار. جعبه‌ابزار من از فریمورک‌های بک‌اند مثل Django و FastAPI تا اپلیکیشن‌های دسکتاپ با PyQt، بینایی ماشین با YOLO و OpenCV و دستیارهای مبتنی بر LLM را در بر می‌گیرد.",
            "cta": "ارتباط با من",
            
        },
        "experience": {"eyebrow": "سابقه کاری", "title": "جاهایی که کار کرده‌ام"}, 
        "certificates": {"eyebrow": "گواهینامه‌ها", "title": "گواهینامه‌ها و افتخارات"},
        "skills_title": "ابزارهایی که با آن‌ها کار می‌کنم",
        "skills": [
            ("Python و Django", 100), ("FastAPI", 95), ("REST و API", 90),
            ("PostgreSQL و MySQL", 85), ("Redis و Celery", 80),
            ("هوش مصنوعی و یادگیری ماشین", 90), ("PyTorch و TensorFlow", 80),
            ("LLM و RAG و OpenAI API", 85), ("بینایی ماشین و YOLO", 90),
            ("OpenCV", 85), ("React", 85), ("TypeScript", 80),
            ("PyQt", 95), ("Docker", 85), ("Git و GitHub", 90),
            ("Linux و CLI", 85), ("CI/CD", 80), ("تست (Pytest)", 85),
        ],
        "work": {
            "eyebrow": "نمونه‌کارها",
            "title": "پروژه‌هایی که به آن‌ها افتخار می‌کنم",
            "label": "کار من",
        },
        "projects": [
            {
                "title": "پلتفرم هوشمند تشخیص عیوب و اشیاء",
                "kind": "پلتفرم بینایی ماشین / هوش مصنوعی",
                "desc": "یک پلتفرم هوشمند بینایی ماشین برای تشخیص عیوب و شناسایی اشیاء با هوش مصنوعی که در ابتدا برای بازرسی پنل‌های خورشیدی توسعه یافته است.",
                "did": "خط پردازش اصلی هوش مصنوعی برای ایجاد دیتاست، برچسب‌گذاری و آموزش چندین مدل را توسعه دادم.",
                "tags": ["بینایی ماشین", "YOLO", "پلتفرم", "هوش مصنوعی"],
                "link": "https://vipatech.ir/projects/",
            },
            {
                "title": "سامانه نظارت تصویری شبکه ریلی",
                "kind": "سیستم نرم‌افزاری / PyQt",
                "desc": "سامانه مدیریت تصاویر واگن‌های قطار، شامل سه بخش نرم‌افزار داخل واگن، واسط و استیشن مرکزی برای دریافت، انتقال و آرشیو ایمن تصاویر.",
                "did": "اپلیکیشن دسکتاپ مبتنی بر PyQt و پروتکل‌های انتقال داده امن را برای پایش ریلی توسعه دادم.",
                "tags": ["PyQt", "اپلیکیشن دسکتاپ", "Python", "پایش"],
                "link": "https://vipatech.ir/projects/rail-image-monitoring/",
            },
            {
                "title": "سامانه نظارت ابعادی و کنترل کیفی پیچ",
                "kind": "بینایی صنعتی / خودکارسازی",
                "desc": "سامانه بینایی ماشین برای کنترل ابعادی و کیفی پیچ‌های صنعتی در خط تولید کارخانه یزدپیچ.",
                "did": "دو دوربین صنعتی را یکپارچه کردم و الگوریتم‌های پردازش تصویر برای اندازه‌گیری و ارسال فرمان به PLC از طریق OPC توسعه دادم.",
                "tags": ["OpenCV", "بینایی صنعتی", "PLC", "Python"],
                "link": "https://vipatech.ir/projects/screw-inspection-system/",
            },
            {
                "title": "دستیار هوشمند صنعت نساجی",
                "kind": "دستیار هوش مصنوعی / LLM",
                "desc": "دستیار هوشمند ویژه صنعت نساجی که کاربران می‌توانند به صورت متنی یا صوتی درباره فرآیندهای تولید و کنترل کیفیت با آن تعامل کنند.",
                "did": "چت‌بات هوش مصنوعی را با استفاده از OpenAI API و ادغام تبدیل گفتار به متن توسعه دادم.",
                "tags": ["LLM", "OpenAI", "چت‌بات", "پردازش زبان طبیعی"],
                "link": "https://vipatech.ir/projects/textile-intelligent-assistant/",
            },
            {
                "title": "سیستم CRM / ERP",
                "kind": "نرم‌افزار سازمانی / Django",
                "desc": "یک راهکار یکپارچه سازمانی برای بهینه‌سازی گردش‌کارها، خودکارسازی مدیریت سفارش، انبار، مالی و حسابداری.",
                "did": "بک‌اند کامل را با Python، Django و PostgreSQL توسعه دادم، با تضمین امنیت، مقیاس‌پذیری و تحلیل داده‌های آنی.",
                "tags": ["Django", "PostgreSQL", "ERP", "بک‌اند"],
                "link": "#",
            },
            {
                "title": "سامانه شمارش لارو آبزیان",
                "kind": "بینایی ماشین / موبایل",
                "desc": "سامانه‌ای مبتنی بر پردازش تصویر که با استفاده از دوربین گوشی، تعداد لاروهای آبزی را با دقت بالا و خودکار شمارش می‌کند.",
                "did": "الگوریتم‌های پردازش تصویر و رابط کاربری موبایل‌پسند را برای شمارش در زمان واقعی توسعه دادم.",
                "tags": ["پردازش تصویر", "OpenCV", "رابط موبایل"],
                "link": "https://vipatech.ir/projects/",
            },
            {
                "title": "بازرسی عیوب سطح ورق فولادی",
                "kind": "هوش مصنوعی صنعتی / زمان واقعی",
                "desc": "بزرگ‌ترین پروژه هوش مصنوعی صنعتی ایران، بازرسی سطح فولاد در زمان واقعی با ۲۴ دوربین صنعتی و سرعت ۲۴۰ فریم بر ثانیه.",
                "did": "خط پردازش بینایی هوش مصنوعی پرسرعت را پیاده‌سازی کردم و هشدارهای عیب را به صورت آنی به اپراتورها رساندم.",
                "tags": ["YOLO", "زمان واقعی", "پرسرعت", "صنعتی"],
                "link": "#",
            },
            {
                "title": "سیستم درجه‌بندی پالت فولادی (آلمان)",
                "kind": "پایش هوشمند / ترکیب سنسور",
                "desc": "یک پروژه صنعتی با تمرکز بر پایش هوشمند و خودکارسازی، اتصال دوربین‌ها و سنسورها برای تشخیص پالت‌های فولادی و اندازه‌گیری فاصله‌ها.",
                "did": "بینایی مبتنی بر هوش مصنوعی و ترکیب سنسور را برای پایش حرکت و پایداری ساختاری با هشدارهای آنی به کار گرفتم.",
                "tags": ["ترکیب سنسور", "بینایی هوش مصنوعی", "خودکارسازی"],
                "link": "#",
            },
        ],
        "reviews": {
            "eyebrow": "نظر همکاران و کارفرماها",
            "title": "کار خوب با همکاری ساخته می‌شود.",
            "items": [
                {"text": "از آن توسعه‌دهنده‌های کمیاب که یک سیستم جاه‌طلبانه را راحت و روان می‌کند. همه تصمیم‌ها فکرشده بود و نتیجه هم پایدار بود هم سریع.", "name": "سارا کریمی", "role": "طراح محصول"},
                {"text": "ارتباطش شفاف است، به موقع تحویل می‌دهد و به جزئیاتی اهمیت می‌دهد که کسی نخواسته بود.", "name": "رضا احمدی", "role": "مدیر پروژه"},
                {"text": "نیازمندی‌های خام ما را در دو هفته به یک راهکار نرم‌افزاری سریع و باکیفیت تبدیل کرد.", "name": "نیما رحیمی", "role": "بنیان‌گذار استارتاپ"},
                {"text": "کد تمیز، تصمیم‌های سنجیده و بدون دردسر. دوباره با او کار می‌کنم.", "name": "مینا حسینی", "role": "توسعه‌دهنده فرانت‌اند"},
            ],
        },
        "contact": {
            "eyebrow": "کار خوب با یک گفتگو شروع می‌شود",
            "title": "آماده ساخت هستید؟",
            "text": "درباره پروژه‌تان بگویید؛ ظرف یک روز پاسخ می‌دهم.",
            "name": "نام و نام خانوادگی", "phone": "شماره تماس", "email": "ایمیل",
            "project": "چه چیزی می‌خواهید بسازید؟", "message": "پیام شما",
            "project_options": [
                "سیستم نرم‌افزاری", "راهکار هوش مصنوعی", "بینایی ماشین / YOLO",
                "اپلیکیشن دسکتاپ (PyQt)", "هوشمندسازی کسب‌وکار", "API و یکپارچه‌سازی", "چیز دیگر"
            ],
            "submit": "ارسال پیام",
            "sending": "در حال ارسال…",
            "success": "ممنون! پیام شما ارسال شد.",
            "error": "مشکلی پیش آمد. فیلدها را بررسی کنید و دوباره تلاش کنید.",
        },
        "footer": "© ۱۴۰۵ میلاد ملتجی. همه حقوق محفوظ است.",
        "ui": {
            "blog": "وبلاگ", "blog_eyebrow": "نوشته‌ها", "blog_title": "یادداشت‌هایی درباره ساختن نرم‌افزار و هوش مصنوعی",
            "blog_text": "مقاله‌های کوتاه درباره مهندسی نرم‌افزار، هوش مصنوعی، خودکارسازی و چیزهایی که در مسیر یاد می‌گیرم.",
            "blog_empty": "هنوز مقاله‌ای نیست. از پنل ادمین یکی اضافه کنید.", "read_more": "خواندن مقاله",
            "back_blog": "همه مقاله‌ها", "back_work": "همه پروژه‌ها", "visit": "مشاهده پروژه",
            "overview": "معرفی", "more_work": "پروژه‌های دیگر", "latest": "از وبلاگ",
            "all_posts": "همه مقاله‌ها",
            "all_projects": "مشاهده همه پروژه‌ها",  # <--- این خط را اضافه کنید
            "pdf": "دانلود PDF", 
            
        },
    },
}





def _pick(obj, field, lang, default=""):
    """مقدار فیلد دوزبانه را برمی‌گرداند، اگر خالی بود از default استفاده می‌کند."""
    val = getattr(obj, f"{field}_{lang}", "") or getattr(obj, f"{field}_{'en' if lang=='fa' else 'fa'}", "")
    return val or default

def get_content(lang):
    """
    محتوای سایت را از دیتابیس می‌خواند و با fallback به CONTENT دیکشنری نهایی می‌سازد.
    رنگ‌ها (THEMES) از فایل می‌مانند.
    """
    from .models import SiteSettings
    s = SiteSettings.load()
    base = CONTENT[lang]
    other_lang = "en" if lang == "fa" else "fa"

    def bi(field, default=""):
        return _pick(s, field, lang, default)

    def jlist(field, default_list, lang_key="fa" if lang == "fa" else "en"):
        """
        یک JsonField که لیستی از dictهاست. هر آیتم ممکن است کلید lang یا کلید مشترک داشته باشد.
        """
        data = getattr(s, field, None)
        if not data:
            return default_list
        return data

    content = {
        "name": bi("name", base["name"]),
        "brand": bi("brand", base["brand"]),
        "title": bi("page_title", base["title"]),
        "lang_label": bi("lang_label", base["lang_label"]),
        "flag": bi("flag", base["flag"]),
        "cta": bi("cta", base["cta"]),

        "nav": [(n.get("id", ""), n.get(lang, n.get("en", ""))) for n in jlist("nav_items", base["nav"])],

        "hero": {
            "eyebrow": bi("hero_eyebrow", base["hero"]["eyebrow"]),
            "hey": bi("hero_hey", base["hero"]["hey"]),
            "line1": bi("hero_line1", base["hero"]["line1"]),
            "line2": bi("hero_line2", base["hero"]["line2"]),
            "text": bi("hero_text", base["hero"]["text"]),
            "link": bi("hero_link", base["hero"]["link"]),
        },

        "stats": [
            (st.get(lang, ""), st.get("label_" + lang, ""))
            for st in jlist("stats", [(n, l) for n, l in base["stats"]])
        ],

        "about": {
            "eyebrow": bi("about_eyebrow", base["about"]["eyebrow"]),
            "title_a": bi("about_title_a", base["about"]["title_a"]),
            "title_b": bi("about_title_b", base["about"]["title_b"]),
            "lead": bi("about_lead", base["about"]["lead"]),
            "text": bi("about_text", base["about"]["text"]),
            "cta": bi("about_cta", base["about"]["cta"]),
        },

        "experience": {
            "eyebrow": bi("exp_eyebrow", base["experience"]["eyebrow"]),
            "title": bi("exp_title", base["experience"]["title"]),
        },
        "certificates": {
            "eyebrow": bi("cert_eyebrow", base["certificates"]["eyebrow"]),
            "title": bi("cert_title", base["certificates"]["title"]),
        },

        "skills_title": bi("skills_title", base["skills_title"]),
        "skills": [
            (sk.get(lang, sk.get("en", "")), sk.get("level", 80))
            for sk in jlist("skills", base["skills"])
        ],

        "work": {
            "eyebrow": bi("work_eyebrow", base["work"]["eyebrow"]),
            "title": bi("work_title", base["work"]["title"]),
            "label": bi("work_label", base["work"]["label"]),
        },

        "projects": base["projects"],  # از مدل Project می‌آید، نه اینجا

        "reviews": {
            "eyebrow": bi("reviews_eyebrow", base["reviews"]["eyebrow"]),
            "title": bi("reviews_title", base["reviews"]["title"]),
            "items": [
                {
                    "text": r.get("text_" + lang, r.get("text_" + other_lang, "")),
                    "name": r.get("name_" + lang, r.get("name_" + other_lang, "")),
                    "role": r.get("role_" + lang, r.get("role_" + other_lang, "")),
                }
                for r in jlist("reviews", base["reviews"]["items"])
            ],
        },

        "contact": {
            "eyebrow": bi("contact_eyebrow", base["contact"]["eyebrow"]),
            "title": bi("contact_title", base["contact"]["title"]),
            "text": bi("contact_text", base["contact"]["text"]),
            "name": bi("contact_name", base["contact"]["name"]),
            "phone": bi("contact_phone", base["contact"]["phone"]),
            "email": bi("contact_email", base["contact"]["email"]),
            "project": bi("contact_project", base["contact"]["project"]),
            "message": bi("contact_message", base["contact"]["message"]),
            "submit": bi("contact_submit", base["contact"]["submit"]),
            "sending": bi("contact_sending", base["contact"]["sending"]),
            "success": bi("contact_success", base["contact"]["success"]),
            "error": bi("contact_error", base["contact"]["error"]),
            "project_options": jlist("project_options", base["contact"]["project_options"]),
        },

        "footer": bi("footer", base["footer"]),

        "ui": {
            "blog": bi("ui_blog", base["ui"]["blog"]),
            "blog_eyebrow": bi("ui_blog_eyebrow", base["ui"]["blog_eyebrow"]),
            "blog_title": bi("ui_blog_title", base["ui"]["blog_title"]),
            "blog_text": bi("ui_blog_text", base["ui"]["blog_text"]),
            "blog_empty": bi("ui_blog_empty", base["ui"]["blog_empty"]),
            "read_more": bi("ui_read_more", base["ui"]["read_more"]),
            "back_blog": bi("ui_back_blog", base["ui"]["back_blog"]),
            "back_work": bi("ui_back_work", base["ui"]["back_work"]),
            "visit": bi("ui_visit", base["ui"]["visit"]),
            "overview": bi("ui_overview", base["ui"]["overview"]),
            "more_work": bi("ui_more_work", base["ui"]["more_work"]),
            "latest": bi("ui_latest", base["ui"]["latest"]),
            "all_posts": bi("ui_all_posts", base["ui"]["all_posts"]),
            "all_projects": bi("ui_all_projects", base["ui"]["all_projects"]),
            "pdf": bi("ui_pdf", base["ui"]["pdf"]),
        },
    }
    return content