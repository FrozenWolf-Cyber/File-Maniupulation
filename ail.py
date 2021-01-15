import os
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle

JK_PATH = 'pic/jk'
TN_PATH = 'pic/tn'
PIC_NAME = 'pic.dat'
TEXT_NAME = 'text.dat'
IMG_W,IMG_H = 700 , 700

jk_images_data = [] 
tn_images_data = [] 

for images in os.listdir(JK_PATH):
    img = cv.imread(JK_PATH+'/'+images)[...,::-1]
    cv.resize(img, (IMG_W, IMG_H),interpolation = cv.INTER_NEAREST)
    jk_images_data.append(img)

for images in os.listdir(TN_PATH):
    img = cv.imread(TN_PATH+'/'+images)[...,::-1]
    cv.resize(img, (IMG_W, IMG_H),interpolation = cv.INTER_NEAREST)
    tn_images_data.append(img)

all_images_data = jk_images_data + tn_images_data

with open(PIC_NAME, 'wb') as fp: 
    pass

with open(PIC_NAME,'ab') as file:
    pickle.dump(all_images_data,file)

location = ['Gulmarg','Srinagar','Pahalgam','kulgam','verinag','ooty','kodaikanal','pichavaram','mudumalai','dhanushkodi']

gulmarg_text = 'Gulmarg is a town, a hill station, a popular skiing destination and a notified area committee in the Baramulla district of Jammu and Kashmir.The town is situated in the Pir Panjal Range in the Western Himalayas and lies within the boundaries of Gulmarg Wildlife Sanctuary.The natural meadows of Gulmarg, which are covered with snow in winter, allow the growth of wild flowers such as daisies, forget-me-nots and buttercups during spring and summer.The meadows are interspersed by enclosed parks and small lakes, and surrounded by forests of green pine and fir.Skiing and other winter sports in Gulmarg are carried out on the slopes of Apharwat peak.'
srinagar_text = 'Srinagar, the summer capital of Jammu and Kashmir is located in the heart of the Kashmir valley at an altitude of 1,730 m above sea level. Spread on both sides of the river Jhelum the city is famous for its natural beauty, gardens, waterfronts and houseboats. Srinagar is called the city of lakes and the Venice of the East, fascinating tourists from centuries with its beautiful picturesque Himalayan backdrop, glittering lakes that are surrounded by houseboats and Shikaras and the majesty of Mughal architecture.The very absence of order in the location of the houses and their tumbled down appearance add a peculiar charm to the scenery. It has its own quaint lifestyle, telling a panoramic fairytale tour through the snow-capped mountains and Chinar trees.'
pahalgam_text = 'Located in the district of Anantnag in the state of Jammu and Kashmir Pahalgam is a place not to be missed upon.Pahalgam is located on the banks of river Lidder. It has a diverse wildlife with green meadows and pristine waters. It is also associated with the Amarnath Yatra which happens annually in the month of July-August.A few species found in Pahalgam include Hangul, Musk Deer, Serow, Rhesus Macaque, Langur, Leopard and Leopard Cat.Culture is another highlight of Pahalgam.Folk dance festival is a grand thing in Pahalgam which is a mix of light music and cultural items like disk, etc.'
kulgam_text = 'Located a few kilometres away from the capital city of Srinagar Kulgam is a town covered by Mt. Pir Panjal with a scenic beauty and vast habitation and culture.Agriculture is the livelihood of several families in Kulgam.In fact, Kulgam is called the Rice Bowl of Kashmir as rice is the major crop there due to its fertile soil and low lying lands apt for the cultivation of rice.Hot springs and Virgin Meadows are some of the attractions in Kulgam.It has tourist spots like "Ahrabal water fall" on Veshev Nallah, Amnoo Eid Gah which is a place of sight-seeing in the extreme south-west of district Kulgam.'
verinag_text = 'Verinag is a tourist place and a notified area committee with tehsil status (Shahabad Bala Verinag) in Anantnag district in the union territory of Jammu and Kashmir. It lies at the entry point of Kashmir Valley right after crossing Jawahar Tunnel and is also known as Gateway of Kashmir.It is situated at the bottom of a hill covered by pine trees and evergreen plants. Verinag spring was originally an irregular and shapeless pond, and water, oozing out from different places in it and spread about and formed a little marsh.Emperor Jahangir, whose artistic taste for polishing the beauty of nature is well known, saw this and at once determined to improve it. He built the octagonal tank of sculptured stones round it, so that all water was collected therein, for which carvers were brought from Iran.'

jk_text = [gulmarg_text,srinagar_text,pahalgam_text,kulgam_text,verinag_text]

ooty_text = 'Ooty , officially known as Udagamandalam , is a town and a municipality in the Nilgiris district of the Indian state of Tamil Nadu. It is a popular hill station located in the Nilgiri Hills.Local residents call it Queen of Hills.Ooty is situated in the Nilgiri Biosphere Reserve.Many of the forested areas and water bodies are off-limits to most visitors in order to protect this fragile ecosystem. Some areas of the Biosphere Reserve have been earmarked for tourism development, and steps are being undertaken to open these areas to visitors whilst conserving the area'
kodaikanal_text = 'Located in the state of Tamil Nadu, Kodaikanal is one of the most amazing destinations in India. A Lakeside resort town of Tamil Nadu, Kodaikanal has a beautiful climate, mist-covered manicured cliffs and waterfall that come together to create the ideal setting for a perfect getaway. Kodaikanal means "the gift of the forests".Nestled amidst the rolling slopes of the Palani Hills, Kodaikanal stands at an altitude of 7200 feet above sea level in Dindugul. It is Very famous for its  Kurinji Flower which blossoms in the area only once every 12 years.'
pichavaram_text = 'Pichavaram Mangrove forest consist of many number of swamp islands  near Chidambaram in Cuddalore District, Tamil Nadu.It consists of a number of islands interspersing a vast expanse of water covered with mangrove forest. The Pichavaram mangrove Forest is one of the largest mangrove forests in India covering about 1100 hectare of area.It is one of the beautiful places in Tamil Nadu which not only attracts many tourists to visit this place but also attracts many kinds of foreign and indigenous birds'
mudumalai_text = 'The Mudumalai National Park and Wildlife Sanctuary also a declared tiger reserve, lies on the northwestern side of the Nilgiri Hills (Blue Mountains), in Nilgiri District, about 150 kilometres north-west of Coimbatore city in Tamil Nadu.The protected area is home to several endangered and vulnerable species including Indian elephant, Bengal tiger, gaur and Indian leopard.One of the most magnificent places located Western Ghats is the hotspot of biological diversity in Southern India. '
dhanushkodi_text = 'Dhanushkodi is a small, sparsely populated beach town on the coast of Tamil Nadu. Dhanushkodi is on the tip of Pamban island, separated from the mainland by the Palk Strait.The clear water and amazing beach is something that one may make one wonder, if any such place exists on the face of earth or not.Bordered by the Bay of Bengal on one side and the Indian Ocean on the other, Dhanushkodi once used to serve as an important port for both traders and pilgrims.'

tn_text = [ooty_text,kodaikanal_text,pichavaram_text,mudumalai_text,dhanushkodi_text]
all_text = jk_text + tn_text

with open(TEXT_NAME, 'wb') as fp: 
    pass

with open(TEXT_NAME,'ab') as file:
    pickle.dump(all_text,file)

image_data = []
text_data = []

with open(PIC_NAME,'rb') as file:
    image_data = pickle.load(file)

with open(TEXT_NAME,'rb') as file:
    text_data = pickle.load(file)


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

index = 0
for i,j,k in zip(image_data,text_data,location): 
    index = index + 1
    if index == 1 and k.upper() == 'GULMARG':
        print(' '*47,color.PURPLE+color.UNDERLINE +'༺ JAMMU AND KASHMIR ༻'+color.END)
    if index == 6:
        print(' '*47,color.PURPLE+color.UNDERLINE +'༺ TAMILNADU ༻'+color.END)
        index = 1
    print(color.PURPLE,str(index)+') ',k.upper()+color.END)
    plt.imshow(i)
    plt.show()
    print(color.RED+j+color.END)
    print('-'*110,end = '\n\n')
