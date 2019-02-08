#This program collects URLs of all the restaurant in Yelp listed for a US city

from selenium import webdriver
import time

#open the browser and visit the url


def runforpage(line,driver):
#Returns the number of restaurants listed in the page.

    driver.get(line)
    #tweet=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[1]/div/div/div[1]/p""")
    tweet=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span""")
    factor=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[1]/div/div/div[1]/p""")
    print(tweet.text)
    print(factor.text)
    pageNum=int(tweet.text.split("of",1)[1])
    factorNum=int((factor.text.split("-",1)[1]).split("of")[0])
    pgnm=int(pageNum)
    print(pgnm)
    fact=int(factorNum/10)
    print(fact)
    return pgnm,fact

def run(line,pgnm,fact):
    
    #This section visits each page for the city and gathers URLs of all the restaurant
    #i=i+1
    b=1
    close=False

    f=open('SanAntonio.txt','w') # output file
    prev=''
	
    for p in range(1,pgnm+1): # for each page 
        
        print ('page',p)
        html=None
        url=''
        

        if p==1: 
            pageLink=line 
            #print(pageLink) # url for page 1       
        else:
            b=fact*(p-1)
            pageLink=line+'&start='+str(b)+'0'# make the page url
        print(pageLink)
        driver.get(pageLink)

        for i in range(1,(fact*10)+1): 
            try:
                restLink=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li["""+str(i)+"""]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a""")
                                                         #//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li[9]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a     
                print(restLink)
                if restLink != []:
                    #link=restLink.find_element_by_xpath("""//*[@href]""")
                    if (restLink.get_attribute('href')):
                        if (restLink.get_attribute("href").find('san-antonio') == -1) or (restLink.get_attribute("href").find('?') != -1):  
                            continue
                        else:
                            url=''
                            url=url+restLink.get_attribute('href')
                            f.write(url+'\n')
                else:
                    close=True
                    break
            except:
                print('No more restaurants')
                close=True
                break
        if close==True:
            break 
    f.close()
    


if __name__=='__main__':
    #i=0    a=0
    line='https://www.yelp.com/search?cflt=restaurants&find_loc=San%20Antonio%2C%20TX'
    driver = webdriver.Chrome('chromedriver.exe')
        
    pgnm,fact=runforpage(line,driver)
    run(line,pgnm,fact)
    driver.quit()


# -*- coding: utf-8 -*-
