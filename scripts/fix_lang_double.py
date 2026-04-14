#!/usr/bin/env python3
"""Fix double <div id="lang-switcher"> wrapper caused by fix_lang_switcher.py
on pages that already had the wrapper."""
import os, re, glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    original = content

    # Replace double wrapper with single
    content = content.replace(
        '<div id="lang-switcher"><div id="lang-switcher">',
        '<div id="lang-switcher">'
    )
    # Fix the extra closing </div> that would result
    # Pattern: </div></div></div> after lang-panel -> </div></div>
    # The structure is: <div#lang-switcher><button/><div#lang-panel>...</div></div>
    # With double open it became: <div><div><button/><div#panel>...</div></div></div>
    # We removed one open, so now: <div><button/><div#panel>...</div></div> - correct

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    html_files = glob.glob('D:/wilsonclassiccar/**/*.html', recursive=True)
    html_files = [f for f in html_files if 'web.archive.org' not in f]
    fixed = sum(1 for f in html_files if fix_file(f))
    print(f"Fixed: {fixed}")

if __name__ == '__main__':
    main()
