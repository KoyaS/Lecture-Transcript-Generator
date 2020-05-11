import sys
import requests
import urllib.request

# unconvertedFileName = 'unconverted.m4a'
# targetFileType = 'wav'
# newFileName = 'newAudio'

# file to be converted MUST be in unconverted audio folder, probably of type .m4a also

def convert(unconvertedFileName, targetFileType):

    newFileName = unconvertedFileName.split('.')[0]
    unconvertedFileName = 'Unconverted_Audio/' + unconvertedFileName
    targetFileType = 'wav'

    print('convertAudio.py: \nConverting - ' + unconvertedFileName + '\nNew file name - ' + newFileName + '\nNew file type - ' + targetFileType)


    """ Unconverted File Name, relative PATH | Target File Type | New File Name """
    url = "https://api2.online-convert.com/jobs"

    print('Sending skeleton...')
    body = "{ \"conversion\": [{        \"category\": \"audio\",        \"target\": \"" + targetFileType + "\"    }] }"
    headers = {
        # 'Host': "api2.online-convert.com",
        'x-oc-api-key': "1b891899156d4f8ebefd26d082dbd9b3",
        'Content-Type': "application/json",
        'Cache-Control': "no-cache"
    }

    response = requests.request("POST", url, data=body, headers=headers)
    # print(response.text, '\n\n')
    print('Skeleton sent')
    jobID = response.json()['id']

    # """ UPLOADING A FILE """

    print('Uploading file...')
    url = response.json()['server'] + "/upload-file/" + response.json()['id']

    payload = {}
    files = [ ('file', open(unconvertedFileName,'rb')) ]
    headers = {
        'x-oc-api-key': '1b891899156d4f8ebefd26d082dbd9b3',
        'Accept': '* / *'
    }

    response = requests.request("POST", url, headers=headers, data = payload, files = files)
    # print(response.text.encode('utf8'),'\n\n')
    print('File uploaded')

    # """ GETTING FINAL PRODUCT """
    print('Waiting on conversion...')
    import time
    time.sleep(5) # To allow server time to process

    url = "https://api2.online-convert.com/jobs/" + jobID

    payload = {}
    headers = {
    'x-oc-api-key': '1b891899156d4f8ebefd26d082dbd9b3'
    }

    # response = requests.request("GET", url, headers = headers, data = payload)
    # print(response.text,'\n\n')

    done = False
    while not done:
        response = requests.request("GET", url, headers = headers, data = payload)
        print('Attempting to get final product...')
        try:
            urllib.request.urlretrieve(response.json()['output'][0]['uri'], ('Converted_Audio/' + newFileName + '.' + targetFileType))
            print('Conversion complete for', newFileName)
            done = True
        except:
            time.sleep(5)
    print('\n'*3)

if __name__ == '__main__':
    unconvertedFileName = sys.argv[1]
    targetFileType = sys.argv[2]

    convert(unconvertedFileName, targetFileType)
