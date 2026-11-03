from django.db import migrations

SLUGS = ["offscript", "frequency", "forma"]


def seed(apps, schema_editor):
    from portfolio.content import CONTENT
    Project = apps.get_model("portfolio", "Project")
    Post = apps.get_model("portfolio", "Post")
    if Project.objects.exists():
        return
    en, fa = CONTENT["en"]["projects"], CONTENT["fa"]["projects"]
    for i, (e, f) in enumerate(zip(en, fa)):
        Project.objects.create(
            slug=SLUGS[i], order=i, link="",
            title_en=e["title"], title_fa=f["title"],
            kind_en=e["kind"], kind_fa=f["kind"],
            desc_en=e["desc"], desc_fa=f["desc"],
            did_en=e["did"], did_fa=f["did"],
            body_en=f"{e['desc']}\n\n{e['did']}", body_fa=f"{f['desc']}\n\n{f['did']}",
            tags_en=", ".join(e["tags"]), tags_fa="، ".join(f["tags"]),
        )
    Post.objects.create(
        slug="hello-world",
        title_en="Hello, world", title_fa="سلام دنیا",
        excerpt_en="Why I started this blog and what you can expect here.",
        excerpt_fa="چرا این وبلاگ را شروع کردم و اینجا چه چیزهایی می‌خوانید.",
        body_en="This is a sample post. Edit or delete it from the admin panel.\n\nWrite about projects, lessons and tools you like. Separate paragraphs with an empty line.",
        body_fa="این یک مقاله‌ی نمونه است. از پنل ادمین می‌توانید آن را ویرایش یا حذف کنید.\n\nدرباره پروژه‌ها، درس‌ها و ابزارهای مورد علاقه‌تان بنویسید. پاراگراف‌ها را با یک خط خالی جدا کنید.",
    )


class Migration(migrations.Migration):
    dependencies = [("portfolio", "0002_post_project")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
