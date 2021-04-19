from bs4 import BeautifulSoup

# How to use in a MAC:
#In chrome use CMD/CTRL shift D to bookmark all tabs and save to a single folder
# option command B to open the bookmarks manager and drill down to the folder
# meatball / overflow menu and export
# save filename as chrome_bookmarks.html (use argparse later on so no hardcoded files needed)


f=open("chrome_bookmarks.html", 'r')
html = f.read()
#print(html)
print("opened bookmarked html of link...")
#html = conn.read()

soup = BeautifulSoup(html, features="lxml")
print("parsing for links...")
links = soup.find_all('a')

#print(links)

all_links = []
for tag in links:
    link = tag.get('href',None)
    if link is not None:
        all_links.append(link)
        #print(link)
#print(all_links)
print("Links discovered...")

with open('bookmarked_links.txt', 'w') as f:
    for item in all_links:
        f.write("%s\n" % item)

print("Links saved as bookmarked_links.txt file")
print("Be sure to change the filename before running this script again or it will overwrite it.")
print("Completed")
