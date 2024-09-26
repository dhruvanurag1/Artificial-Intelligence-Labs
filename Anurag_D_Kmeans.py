''' Test cases:
6 https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg
10 cute_dog.jpg
6 turtle.jpg
'''
from itertools import count
import PIL
from PIL import Image
import urllib.request
import io, sys, os, random
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

visited = set()

def choose_random_means(k, img, pix):
   means = [pix[random.randrange(img.size[0]),random.randrange(img.size[1])] for a in range(k)]
   return means

# goal test: no hopping
def check_move_count(mc): 
   return mc.count(0) == len(mc)

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means):
   dists = [(col[0] - means[a][0]) ** 2 + (col[1] - means[a][1]) ** 2 + (col[2] - means[a][2]) ** 2 for a in range(len(means))]
   return dists.index(min(dists)) 
 
def clustering(img, pix, cb, mc, means, count):
   temp_pb, temp_mc, temp_m = [[] for x in means], [], []
   temp_cb = [0 for x in means]
   for a in range(img.size[0]):
      for b in range(img.size[1]):
         minimum = dist(pix[a, b], means)
         temp_cb[minimum] += 1
         temp_pb[minimum].append(pix[a,b])
   temp_m = [(sum(a[0] for a in x)/len(x), sum(a[1] for a in x)/len(x), sum(a[2] for a in x)/len(x)) for x in temp_pb]
   temp_mc = [ (a-b) for a, b in zip(temp_cb, cb)]
   #print ('diff', count, ':', temp_mc)
   return temp_cb, temp_mc, temp_m

def update_picture(img, pix, means):
   region_dict = {}
   for a in range(img.size[0]):
      for b in range(img.size[1]):
         min = dist(pix[a,b], means)
         pix[a, b] = (int(means[min][0]), int(means[min][1]), int(means[min][2]))
   return pix, region_dict
   
def distinct_pix_count(img, pix):
   dict = {}
   for a in range(img.size[0]):
       for b in range(img.size[1]):
           if pix[a,b] not in dict.keys(): dict[pix[a,b]] = 1
           else: dict[pix[a,b]] += 1
   max_col, max_count = max(dict, key=dict.get), dict[max(dict, key=dict.get)]
   return len(dict.keys()), max_col, max_count

def count_regions(img, region_dict, pix, means):
   region_count = [0 for x in means]
   for a in range(img.size[0]):
      for b in range(img.size[1]):
         if (a,b) not in visited:
            floodfill_helper(img, pix, pix[a,b], a, b, means)
            #print(len(visited))
            #print("HI")
            region_count[dist(pix[a,b], means)] += 1
   return region_count
def floodfill_helper(img, pix, col, a, b, means): #make a floodfill helper function
   if (a, b) in visited or a > img.size[0] or a < 0 or b > img.size[1] or b < 0 or pix[a,b] != col: return
   #count += 1
   #print(count)

   #print(pix[a, b])
   #print(len(visited))
   visited.add((a, b))
   fillers = set()
   fillers.add((a, b))
   while len(fillers) != 0:
       a, b = fillers.pop()
       if a >= img.size[0] or a < 0 or b >= img.size[1] or b < 0 or pix[a,b] != col: 
           continue
       visited.add((a,b))
       if((a-1, b-1) not in visited): fillers.add((a-1, b-1))
       if((a, b-1) not in visited):  fillers.add((a, b-1))
       if((a+1, b-1) not in visited): fillers.add((a+1, b-1))
       if((a-1, b) not in visited): fillers.add((a-1, b))
       if((a+1, b) not in visited): fillers.add((a+1, b))
       if((a-1, b+1) not in visited): fillers.add((a-1, b+1))
       if((a, b+1) not in visited): fillers.add((a, b+1))
       if((a+1, b+1) not in visited): fillers.add((a+1, b+1))

#    if((a-1, b-1) not in visited): floodfill_helper(img, pix, col, a-1, b-1, means)
#    if((a, b-1) not in visited): floodfill_helper(img, pix, col, a, b-1, means)
#    if((a+1, b-1) not in visited): floodfill_helper(img, pix, col, a+1, b-1, means)
#    if((a-1, b) not in visited): floodfill_helper(img, pix, col, a-1, b, means)
#    if((a+1, b) not in visited): floodfill_helper(img, pix, col, a+1, b, means)
#    if((a-1, b+1) not in visited): floodfill_helper(img, pix, col, a-1, b+1, means)
#    if((a, b+1) not in visited): floodfill_helper(img, pix, col, a, b+1, means)
#    if((a+1, b+1) not in visited): floodfill_helper(img, pix, col, a+1, b+1, means)
 
def main():
   k = int(sys.argv[2])
   file = sys.argv[1]
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   
   window = tk.Tk() #create an window object
   
   img = Image.open(file)
   
   # img_tk = ImageTk.PhotoImage(img)
   # lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = choose_random_means(k, img, pix)
   #print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = clustering(img, pix, count_buckets, move_count, means, count)
    #   if count == 2:
    #      print ('first means:', means)
    #      print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means)  # region_dict can be an empty dictionary
   #print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (str(i+1) + ':', means[i], '=>', count_buckets[i])
      
   imagefile = "cute_dog.jpg"
   imng = ImageTk.PhotoImage(Image.open(imagefile))
   lbl1 = tk.Label(window, image = imng).pack()

   img_tk = ImageTk.PhotoImage(img)
   lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   
   print('Region counts:', str(count_regions(img, region_dict, pix, means))[1:-1])

   img.save('kmeans.png', 'PNG')  # change to your own filename
   window.mainloop()
   #img.show()
   
if __name__ == '__main__': 
   main()