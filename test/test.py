# coding: utf-8
from bs4 import BeautifulSoup


text = """class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:Comics">Comics</a>‎ <span dir="ltr" title="Contains 1 subcategory, 7 pages, and 0 files">(7 articles; 1 subcategory)</span></div>
<div class="CategoryTreeChildren" style="display:none"></div></div>
</li>
<li><div class="CategoryTreeSection"><div class="CategoryTreeItem"><span class="CategoryTreeEmptyBullet">► </span> <a class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:Creative_Taiwan">Creative Taiwan</a>‎ <span dir="ltr" title="Contains 0 subcategories, 2 pages, and 0 files">(2 articles)</span></div>
<div class="CategoryTreeChildren" style="display:none"></div></div>
</li></ul></div><div class="mw-category-group"><h3>D</h3>
<ul><li><div class="CategoryTreeSection"><div class="CategoryTreeItem"><span class="CategoryTreeEmptyBullet">► </span> <a class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:Dance">Dance</a>‎ <span dir="ltr" title="Contains 0 subcategories, 14 pages, and 0 files">(14 articles)</span></div>
<div class="CategoryTreeChildren" style="display:none"></div></div>
</li>
<li><div class="CategoryTreeSection"><div class="CategoryTreeItem"><span class="CategoryTreeEmptyBullet">► </span> <a class="CategoryTreeLabel CategoryTreeLabelNs14 CategoryTreeLabelCategory" href="/wiki/Category:Doctor_Who">Doctor Who</a>‎ <span dir="ltr" title="Contains 0 subcategories, 10 pages, and 0 files">(10 articles)</span></div>
<div class="CategoryTreeChildren" style="display:none"></div></div>
</li>
"""

soup = BeautifulSoup(text)
for a in soup.find_all("a"):
    print a['href']
