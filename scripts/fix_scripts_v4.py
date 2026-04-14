#!/usr/bin/env python3
"""
Fix Round 4: Properly wrap floating var declarations in <script> tags.
The \x02 control character sits between </script> and the floating var content.

Current broken structure (with \x02 shown as STX):
  <script src="ajax.js"></script>STX\nvar joltnews_custom = {...};\n</script>\n
  <script src="custom.js"></script>STX\nvar joltnews_pagination = {...};\n</script>\n
  <script src="pagination.js"></script>STX\nvar fifuImageVars = {...};\n</script>\n
  <script src="image.js"></script>STX><button ...

Target structure:
  <script src="ajax.js"></script>
  <script id="joltnews-custom-js-extra">
  var joltnews_custom = {...};
  </script>
  <script src="custom.js"></script>
  <script id="joltnews-pagination-js-extra">
  var joltnews_pagination = {...};
  </script>
  <script src="pagination.js"></script>
  <script id="fifu-image-js-js-extra">
  var fifuImageVars = {...};
  </script>
  <script src="image.js"></script>
  <button ...
"""

import os
import re
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # Fix 1: Wrap floating joltnews_custom var block
    # Pattern: ajax.js"></script>\x02\nvar joltnews_custom = ...;\n</script>\n
    content = re.sub(
        r'(ajax\.js"></script>)\x02\n(var joltnews_custom = .+?;\n)(</script>\n)',
        r'\1\n<script id="joltnews-custom-js-extra">\n\2\3',
        content,
        flags=re.DOTALL
    )

    # Fix 2: Wrap floating joltnews_pagination var block
    content = re.sub(
        r'(custom\.js"></script>)\x02\n(var joltnews_pagination = .+?;\n)(</script>\n)',
        r'\1\n<script id="joltnews-pagination-js-extra">\n\2\3',
        content,
        flags=re.DOTALL
    )

    # Fix 3: Wrap floating fifuImageVars var block
    content = re.sub(
        r'(pagination\.js"></script>)\x02\n(var fifuImageVars = .+?;\n)(</script>\n)',
        r'\1\n<script id="fifu-image-js-js-extra">\n\2\3',
        content,
        flags=re.DOTALL
    )

    # Fix 4: Remove \x02> after image.js closing tag: "></script>\x02><button
    content = re.sub(
        r'(image\.js"></script>)\x02>(<button)',
        r'\1\n\2',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    base_dir = 'D:/wilsonclassiccar'
    html_files = glob.glob(os.path.join(base_dir, '**/*.html'), recursive=True)

    # Exclude web.archive.org folder
    html_files = [f for f in html_files if 'web.archive.org' not in f]

    fixed = 0
    skipped = 0
    for filepath in sorted(html_files):
        if fix_file(filepath):
            fixed += 1
        else:
            skipped += 1

    print(f"Fixed: {fixed}, Skipped (no change): {skipped}")

if __name__ == '__main__':
    main()
