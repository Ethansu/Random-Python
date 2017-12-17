from medpy.io import load
import numpy as np
import os
import h5py


for i in range(10):
    subject_name = 'subject-%d-' % (i + 1)
    f_C = os.path.join(data_path, subject_name + 'C.hdr')
    img_C, header_C = load(f_C)

    inputs = img_C.astype(np.float32)
#same for second input 
    A = inputs.shape[0]     #142
    B = inputs.shape[1]     # 176
    C = inputs.shape[2]     # 181
    D = np.arange(A*B*C).reshape(A,B,C)
    print (D.shape)
