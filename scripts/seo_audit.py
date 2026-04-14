import sys, re, os, glob
sys.stdout.reconfigure(encoding='utf-8')

base = 'D:/wilsonclassiccar'
LANGS = {'ar','cs','de','el','es','fi','fr','hi','it','ja','ko','nl','pl','pt','ro','ru','sk','sv','tr','uk','zh'}

all_html = glob.glob(base + '/**/index.html', recursive=True)
all_html = [f for f in all_html if 'web.archive.org' not in f]

def is_lang_page(fp):
    parts = fp.replace('\\', '/').split('/')
    for p in parts:
        if p in LANGS:
            return True
    return False

def is_feed(fp):
    fp2 = fp.replace('\\', '/')
    return '/feed/' in fp2 or '/comments/' in fp2

en_pages_real = [f for f in all_html if not is_lang_page(f) and not is_feed(f)]

lang_dirs = [d for d in os.listdir(base) if os.path.isdir(os.path.join(base, d)) and d in LANGS]

print(f"Total HTML files (excl. web.archive.org): {len(all_html)}")
print(f"EN pages (excl. feed/comments): {len(en_pages_real)}")
print(f"Languages: {len(lang_dirs)} ({', '.join(sorted(lang_dirs))})")

missing_title = missing_desc = missing_h1 = missing_canon = missing_og = 0
has_schema = no_schema = 0
has_breadcrumb = 0
thin_content = 0
broken_imgs = 0

for fp in en_pages_real:
    with open(fp, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    if not re.search(r'<title>[^<]+</title>', content): missing_title += 1
    if not re.search(r'<meta name="description"[^>]*content="[^"]+"', content): missing_desc += 1
    if not re.search(r'<h1[^>]*>[^<]+</h1>', content, re.DOTALL): missing_h1 += 1
    if not re.search(r'rel="canonical"[^>]*href="[^"]+"', content): missing_canon += 1
    if not re.search(r'property="og:image"[^>]*content="[^"]+"', content) and \
       not re.search(r'content="[^"]+"[^>]*property="og:image"', content): missing_og += 1
    if 'application/ld+json' in content: has_schema += 1
    else: no_schema += 1
    if 'BreadcrumbList' in content: has_breadcrumb += 1
    body_text = re.sub(r'<[^>]+>', ' ', content)
    body_text = re.sub(r'\s+', ' ', body_text).strip()
    if len(body_text.split()) < 300: thin_content += 1

# Check RSS feed files
rss_files = glob.glob(base + '/feed/index.html')
rss_count = len(rss_files)

print(f"\nSEO Metrics across {len(en_pages_real)} EN pages:")
print(f"Missing title: {missing_title}")
print(f"Missing description: {missing_desc}")
print(f"Missing H1: {missing_h1}")
print(f"Missing canonical: {missing_canon}")
print(f"Missing OG image: {missing_og}")
print(f"Has schema: {has_schema} | No schema: {no_schema}")
print(f"Has BreadcrumbList: {has_breadcrumb}")
print(f"Thin content (<300 words): {thin_content}")
print(f"RSS feed files: {rss_count}")

# Check sitemap.xml
sitemap = os.path.exists(os.path.join(base, 'sitemap.xml'))
robots = os.path.exists(os.path.join(base, 'robots.txt'))
print(f"Sitemap.xml: {'YES' if sitemap else 'NO'}")
print(f"Robots.txt: {'YES' if robots else 'NO'}")

# Structured data type
with open(os.path.join(base, 'index.html'), 'r', encoding='utf-8') as f:
    idx = f.read()
schema_types = re.findall(r'"@type"\s*:\s*"([^"]+)"', idx)
print(f"Schema types (homepage): {schema_types}")
