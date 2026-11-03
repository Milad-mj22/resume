"""
تمام متن‌های سایت اینجاست. برای تغییر اسم، پروژه‌ها، نظرات و ... فقط همین فایل را ویرایش کنید.
"""

DEFAULT_LANG = "fa"

CONTENT = {
    # ------------------------------------------------------------------ English
    "en": {
        "name": "Milad Moltaji",
        "brand": "Milad Moltaji",
        "title": "Milad Moltaji — Developer",
        "lang_label": "English",
        "flag": "🇺🇸",
        "nav": [
            ("about", "About"),
            ("skills", "Skills"),
            ("work", "Selected work"),
            ("reviews", "Reviews"),
        ],
        "cta": "Get in touch",
        "hero": {
            "eyebrow": "Portfolio",
            "hey": "Hey, I'm a",
            "line1": "",
            "line2": "Developer",
            "text": "I build responsive, accessible websites where thoughtful design meets clean code.",
            "link": "Explore my projects",
        },
        "stats": [
            ("6", "Years of experience"),
            ("15", "Projects shipped"),
            ("15", "Happy clients"),
            ("95", "Lighthouse score"),
        ],
        "about": {
            "eyebrow": "Behind the work",
            "title_a": "Building experiences.",
            "title_b": "Making them click.",
            "lead": "I'm a front-end developer turning ambitious ideas into clear, intuitive interfaces.",
            "text": "From the first sketch to the final interaction, I care about every detail: how a page looks, how it feels, and how smoothly it works for everyone.",
            "cta": "Get in touch",
        },
        "skills_title": "Tools I reach for",
        "skills": [
            ("HTML & CSS", 95), ("JavaScript", 90), ("Vue / React", 85),
            ("Django", 70), ("Tailwind", 90), ("Figma", 75),
        ],
        "work": {
            "eyebrow": "Selected work",
            "title": "Projects I'm proud of",
            "label": "What I did",
        },
        "projects": [
            {
                "title": "Offscript",
                "kind": "Portfolio platform / Vue",
                "desc": "A showcase platform for independent creators, built around fast navigation and clean layouts.",
                "did": "Designed the layout system, built reusable components and a fast, accessible interface.",
                "tags": ["Responsive UI", "Components", "Vue"],
                "link": "#",
            },
            {
                "title": "Frequency",
                "kind": "Interactive web experience / Vue",
                "desc": "A concept storefront for independent outerwear, designed to make browsing feel effortless on every screen.",
                "did": "Created a flexible product grid, clear category navigation and a mobile-first shopping flow.",
                "tags": ["Responsive UI", "Product discovery", "Vue"],
                "link": "#",
            },
            {
                "title": "Forma",
                "kind": "Photography showcase / CSS",
                "desc": "An editorial gallery for photographers, where images lead and the interface stays out of the way.",
                "did": "Built a masonry gallery with smooth transitions and optimized image loading.",
                "tags": ["Gallery", "Performance", "CSS"],
                "link": "#",
            },
        ],
        "reviews": {
            "eyebrow": "Colleague & client reviews",
            "title": "Better work happens together.",
            "items": [
                {"text": "The rare kind of developer who makes an ambitious design feel effortless to use. Every interaction felt intentional, and the result was as fast as it was beautiful.", "name": "Sara Karimi", "role": "Product Designer"},
                {"text": "Communicates clearly, delivers on time and cares about the details nobody asked for.", "name": "Reza Ahmadi", "role": "Project Manager"},
                {"text": "He turned our rough Figma file into a polished, fast website in two weeks.", "name": "Nima Rahimi", "role": "Startup Founder"},
                {"text": "Clean code, thoughtful decisions and zero drama. I'd work with him again.", "name": "Mina Hosseini", "role": "Back-End Developer"},
            ],
        },
        "contact": {
            "eyebrow": "Good work starts with a conversation",
            "title": "Ready to build?",
            "text": "Tell me about your project and I'll get back to you within a day.",
            "name": "Your name", "phone": "Your number", "email": "Your email",
            "project": "What do you want to build?", "message": "Message",
            "project_options": ["Landing page", "Company website", "Web app", "Redesign", "Something else"],
            "submit": "Send message",
            "sending": "Sending…",
            "success": "Thanks! Your message was sent.",
            "error": "Something went wrong. Check the fields and try again.",
        },
        "footer": "© 2026 Amirhossein Amouzgar. All rights reserved.",
    },

    # ------------------------------------------------------------------ Persian
    "fa": {
        "name": "میلاد ملتحی",
        "brand": "میلاد ملتحی",
        "title": "میلاد ملتحی — توسعه‌دهنده هوش مصنوعی ، بک‌اند و هوشمند سازی کسب و کار",
        "lang_label": "فارسی",
        "flag": "🇮🇷",
        "nav": [
            ("about", "درباره"),
            ("skills", "مهارت‌ها"),
            ("work", "نمونه‌کارها"),
            ("reviews", "نظرها"),
        ],
        "cta": "ارتباط با من",
        "hero": {
            "eyebrow": "پورتفولیو",
            "hey": "سلام، من یک",
            "line1": "توسعه‌دهنده",
            "line2": " هستم",
            "text": "سایت‌هایی ریسپانسیو و در دسترس می‌سازم که طراحی فکرشده و کد تمیز کنار هم قرار می‌گیرند.",
            "link": "پروژه‌هایم را ببینید",
        },
        "stats": [
            ("۶", "سال تجربه"),
            ("۱۵", "پروژه تحویل‌شده"),
            ("۱۵", "کارفرمای راضی"),
            ("۹۵", "امتیاز لایت‌هاوس"),
        ],
        "about": {
            "eyebrow": "پشت صحنه کار",
            "title_a": "ساختن تجربه‌هایی",
            "title_b": "که روان کار می‌کنند.",
            "lead": "سازنده رابط‌های کاربری‌ای که کارکردشان به زیبایی ظاهرشان است.",
            "text": "از اولین طرح تا آخرین تعامل، به همه جزئیات اهمیت می‌دهم: ظاهر صفحه، حس استفاده و روان‌بودن آن برای همه.",
            "cta": "ارتباط با من",
        },
        "skills_title": "ابزارهایی که با آن‌ها کار می‌کنم",
        "skills": [
            ("HTML و CSS", 95), ("JavaScript", 90), ("Vue / React", 85),
            ("Django", 70), ("Tailwind", 90), ("Figma", 75),
        ],
        "work": {
            "eyebrow": "نمونه‌کارها",
            "title": "پروژه‌هایی که به آن‌ها افتخار می‌کنم",
            "label": "کار من",
        },
        "projects": [
            {
                "title": "Offscript",
                "kind": "پلتفرم نمونه‌کار / Vue",
                "desc": "پلتفرم معرفی آثار برای خالقان مستقل، با ناوبری سریع و چیدمان تمیز.",
                "did": "سیستم چیدمان را طراحی کردم و کامپوننت‌های قابل‌استفاده‌مجدد و رابطی سریع و در دسترس ساختم.",
                "tags": ["رابط ریسپانسیو", "کامپوننت", "Vue"],
                "link": "#",
            },
            {
                "title": "Frequency",
                "kind": "تجربه وب تعاملی / Vue",
                "desc": "یک فروشگاه مفهومی برای پوشاک مستقل که گشت‌وگذار را روی هر صفحه‌ای راحت می‌کند.",
                "did": "شبکه محصول منعطف، ناوبری دسته‌بندی روشن و مسیر خرید موبایل‌محور ساختم.",
                "tags": ["رابط ریسپانسیو", "کشف محصول", "Vue"],
                "link": "#",
            },
            {
                "title": "Forma",
                "kind": "نمایشگاه عکاسی / CSS",
                "desc": "گالری تحریریه‌ای برای عکاسان؛ جایی که تصویر اصل است و رابط کنار می‌ایستد.",
                "did": "گالری مسونری با انیمیشن‌های نرم و بارگذاری بهینه تصاویر ساختم.",
                "tags": ["گالری", "کارایی", "CSS"],
                "link": "#",
            },
        ],
        "reviews": {
            "eyebrow": "نظر همکاران و کارفرماها",
            "title": "کار خوب با همکاری ساخته می‌شود.",
            "items": [
                {"text": "از آن توسعه‌دهنده‌های کمیاب که یک طراحی جاه‌طلبانه را راحت و روان می‌کند. همه تعامل‌ها فکرشده بود و نتیجه هم سریع بود هم زیبا.", "name": "سارا کریمی", "role": "طراح محصول"},
                {"text": "ارتباطش شفاف است، به موقع تحویل می‌دهد و به جزئیاتی اهمیت می‌دهد که کسی نخواسته بود.", "name": "رضا احمدی", "role": "مدیر پروژه"},
                {"text": "فایل خام فیگمای ما را در دو هفته به یک سایت سریع و باکیفیت تبدیل کرد.", "name": "نیما رحیمی", "role": "بنیان‌گذار استارتاپ"},
                {"text": "کد تمیز، تصمیم‌های سنجیده و بدون دردسر. دوباره با او کار می‌کنم.", "name": "مینا حسینی", "role": "توسعه‌دهنده بک‌اند"},
            ],
        },
        "contact": {
            "eyebrow": "کار خوب با یک گفتگو شروع می‌شود",
            "title": "آماده ساخت هستید؟",
            "text": "درباره پروژه‌تان بگویید؛ ظرف یک روز پاسخ می‌دهم.",
            "name": "نام و نام خانوادگی", "phone": "شماره تماس", "email": "ایمیل",
            "project": "چه چیزی می‌خواهید بسازید؟", "message": "پیام شما",
            "project_options": ["صفحه فرود", "سایت شرکتی", "وب‌اپلیکیشن", "بازطراحی", "چیز دیگر"],
            "submit": "ارسال پیام",
            "sending": "در حال ارسال…",
            "success": "ممنون! پیام شما ارسال شد.",
            "error": "مشکلی پیش آمد. فیلدها را بررسی کنید و دوباره تلاش کنید.",
        },
        "footer": "© ۱۴۰۵ امیرحسین آموزگار. همه حقوق محفوظ است.",
    },
}


CONTENT["en"]["ui"] = {
    "blog": "Blog", "blog_eyebrow": "Writing", "blog_title": "Notes on building for the web",
    "blog_text": "Short articles about front-end work, design details and what I learn along the way.",
    "blog_empty": "No posts yet. Add one from the admin panel.", "read_more": "Read article",
    "back_blog": "All articles", "back_work": "All projects", "visit": "Visit project",
    "overview": "Overview", "more_work": "More projects", "latest": "From the blog",
    "all_posts": "View all articles",
}
CONTENT["fa"]["ui"] = {
    "blog": "وبلاگ", "blog_eyebrow": "نوشته‌ها", "blog_title": "یادداشت‌هایی درباره ساختن برای وب",
    "blog_text": "مقاله‌های کوتاه درباره فرانت‌اند، جزئیات طراحی و چیزهایی که در مسیر یاد می‌گیرم.",
    "blog_empty": "هنوز مقاله‌ای نیست. از پنل ادمین یکی اضافه کنید.", "read_more": "خواندن مقاله",
    "back_blog": "همه مقاله‌ها", "back_work": "همه پروژه‌ها", "visit": "مشاهده پروژه",
    "overview": "معرفی", "more_work": "پروژه‌های دیگر", "latest": "از وبلاگ",
    "all_posts": "همه مقاله‌ها",
}
