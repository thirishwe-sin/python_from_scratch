from urllib.request import urlretrieve

link = input('Image download link: ')

fileName = input('File name: ')

urlretrieve(link, 'image/'+fileName+'.jpg')

