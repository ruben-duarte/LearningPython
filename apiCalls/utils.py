import time
import lzma
import gzip
import bz2

# data = b'This is a sample data'*8230000

# ==== lzma
# print('original data size: ', len(data))
# print('lzma')
# start = time.time()
# compressed_data_lzma = lzma.compress(data)
# end = time.time()

# print(end - start)
# print(len(compressed_data_lzma))
#print(lzma.decompress(compressed_data_lzma))

# ==== gzip 
# print('gzip')
# start = time.time()
# compressed_data_gzip = gzip.compress(data)
# gzip = gzip.compress(data, compresslevel=1)
# end = time.time()

# print(end - start)
# print(len(compressed_data_gzip))
# print(gzip.decompress(gzip))

# ==== bz2 
# print('bz2')
# start = time.time()
# gzip = bz2.compress(data)
# end = time.time()

# print(end - start)
# print(len(compressed_data_lzma))
#print(bz2.decompress(bz2))

with open('someText.txt', 'rb') as f_in, gzip.open('someFile.gz' , 'wb') as f_out:
    f_out.write(f_in.read())
