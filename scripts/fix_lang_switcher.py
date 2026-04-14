#!/usr/bin/env python3
"""
Fix language switcher:
1. Add missing <div id="lang-switcher"> wrapper before <button id="lang-btn">
2. Move switcher to left side: right:20px -> left:20px, panel right:0 -> left:0
"""
import os, re, glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Fix 1: Add wrapper div before the button (it's missing but closing </div> exists)
    content = re.sub(
        r'(<button id="lang-btn">)',
        r'<div id="lang-switcher">\1',
        content
    )

    # Fix 2: Move to left side in CSS
    content = content.replace(
        '#lang-switcher{position:fixed;bottom:20px;right:20px;z-index:9999;font-family:sans-serif}',
        '#lang-switcher{position:fixed;bottom:20px;left:20px;z-index:9999;font-family:sans-serif}'
    )
    content = content.replace(
        '#lang-panel{display:none;position:absolute;bottom:44px;right:0;background:#fff;',
        '#lang-panel{display:none;position:absolute;bottom:44px;left:0;background:#fff;'
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = 'D:/wilsonclassiccar'
    html_files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)
    html_files = [f for f in html_files if 'web.archive.org' not in f]

    fixed = skipped = 0
    for filepath in sorted(html_files):
        if fix_file(filepath):
            fixed += 1
        else:
            skipped += 1

    print(f"Fixed: {fixed}, Skipped: {skipped}")

if __name__ == '__main__':
    main()
