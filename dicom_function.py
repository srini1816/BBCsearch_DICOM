import os
import pydicom
from samples.ctscan import ds
from pydicom.dataset import Dataset


dataset = pydicom.dcmread("C:/dicom/ttfm.dcm")


#Below function to modify the value of any element by retrieving it and setting the value

elem = ds[0x0010, 0x0010]
elem.value
'CompressedSamples, CT1'
elem.value = 'Citizen Jan'
print(elem)

#Multi-valued elements can be set using a list or modified using the list methods:

ds.ImageType = ['ORIGINAL', 'PRIMARY', 'LOCALIZER']
ds.ImageType[1] = 'DERIVED'
ds.ImageType.insert(1, 'PRIMARY')
print(ds)

#for sequence elements:

ds.OtherPatientIDsSequence = [Dataset(), Dataset()]
ds.OtherPatientIDsSequence.append(Dataset())
len(ds.OtherPatientIDsSequence)
print(ds)

