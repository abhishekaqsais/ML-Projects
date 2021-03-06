# -*- coding: utf-8 -*-
"""
This program takes URL page as input and creates data file for each of the restaurant listed in the URL page
Created on Sat Nov  3 16:56:17 2018

@author: Abhishek Anand
"""

from selenium import webdriver
import time
import requests

def run(line,a,driver):
    
    i=1
    f=open('gfk_'+str(a)+'.txt','w') # output file
	        
    #driver = webdriver.Chrome('chromedriver.exe')
    try:
        driver.get(line)
    except:
        print('No more URLs')
    
    #restaurant name
    try:     
        name=driver.find_element_by_xpath("""//*[@id="wrap"]/div[2]/div/div[1]/div/div[3]/div[1]/div[1]/h1""")
        f.write(name.text+'\n')
    except:
        try:
            name=driver.find_element_by_xpath("""//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div[1]/h1""")
            f.write(name.text+'\n')
        except:            
            print('No restaurants!')
    
    #restaurant type
    while True:
        try:
            rtype=driver.find_element_by_xpath("""//*[@id="wrap"]/div[2]/div/div[1]/div/div[3]/div[1]/div[2]/div[2]/span[2]/a["""+str(i)+"""]""")
            f.write(rtype.text+'\t')
            i=i+1
        except:
            try:
                rtype=driver.find_element_by_xpath("""//*[@id="wrap"]/div[2]/div/div[1]/div/div[4]/div[1]/div[2]/div[2]/span[2]/a["""+str(i)+"""]""")
                f.write(rtype.text+'\t')
                i=i+1
            except:            
                print('No further specifications!')
                break
    f.write('\n')

    timings=driver.find_elements_by_xpath("//table[contains(@class,'hours-table')]//tr")
    for hours in timings:
        try:
            raw_day = hours.find_element_by_xpath(".//th")
            raw_timing = hours.find_element_by_xpath("./td")
            f.write(raw_day.text+'\t'+raw_timing.text+'\n')
        except:
            print('No further specifications!')
            continue
      
    i=1
     #review highlights   
    while True:
        try:
                                              
            rhighlights=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[1]/div[1]/div[1]/ul/li["""+str(i)+"""]/div[2]/p""")
            #print(rhighlights)
            f.write(rhighlights.text+'\n')
            i=i+1
        except:
            c=i
            print('No further specifications!')
            break
    
    try:      
        driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[1]/div[1]/div[1]/div""")
        a.find_element_by_partial_link_text('Show more review highlights').click()
    except:
        print('No more review highlights!')
    
    c=c+1
    while True:
        try:
                                              
            rhighlights1=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[1]/div[1]/div[1]/ul/li["""+str(i)+"""]/div[2]/p""")
            #print(rhighlights)
            f.write(rhighlights1.text+'\n')
            c=c+1
        except:
            print('No further specifications!')
            break
        
    
    i=1
     #business info and response   
    while True:
        try:
                                                 
            binfo=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[2]/div[2]/div[2]/ul/li/div/dl["""+str(i)+"""]/dt""")
            reply=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[2]/div[2]/div[2]/ul/li/div/dl["""+str(i)+"""]/dd""")
            if binfo.text != 'Good for Kids':
                f.write(binfo.text+'\t'+reply.text+'\n')
            i=i+1
        except:
            try:
                binfo=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[2]/div[2]/div[3]/ul/li/div/dl["""+str(i)+"""]/dt""")
                reply=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[2]/div[2]/div[3]/ul/li/div/dl["""+str(i)+"""]/dd""")
                if binfo.text != 'Good for Kids':
                    f.write(binfo.text+'\t'+reply.text+'\n')
                i=i+1
            except:
                
                print('No further specifications!')
                break
    
    
    i=2
     #reviews   
    while True:
        try:
            try:
                review=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[1]/div[2]/div[2]/div[2]/ul/li["""+str(i)+"""]/div/div[2]/div[1]/p""")
                f.write(review.text+'\n')
                i=i+1
            except:
                                                  
                review=driver.find_element_by_xpath("""//*[@id="super-container"]/div[1]/div/div[1]/div[3]/div[2]/div[2]/ul/li["""+str(i)+"""]/div/div[2]/div[1]/p""")
                f.write(review.text+'\n')
                i=i+1
        except:
            print('No further specifications!')
            break

    

    f.close()
    

if __name__=='__main__':

    a=0
    fw=open('SanAntonio.txt','r')
    driver = webdriver.Chrome('chromedriver.exe')
    lines=fw.readlines()
    for line in lines:
        a=a+1
        run(line,a,driver)
    fw.close()
    driver.quit()
        


