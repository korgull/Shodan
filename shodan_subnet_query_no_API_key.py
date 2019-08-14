import shodan
import sys
import os
import time

SHODAN_API_KEY = "[PUT API KEY HERE]"

api = shodan.Shodan(SHODAN_API_KEY)
if (len(sys.argv) < 2 or len(sys.argv) > 2):
        print("\nNot enough arguments.\nThis script takes in a file with a list of IP addresses or subnets\nUsage:  python3 shodan.py [file with IP subnets]\n")
        sys.exit(0)

file = sys.argv[1]        

filename = os.path.splitext(sys.argv[1])[0]
ext = os.path.splitext(sys.argv[1])[1]

newfilename = str(filename) + "_shodan_results.txt"

resultfile = open(newfilename, 'w') #variable just here to create the file
resultfile.close()

print("Created " + newfilename + " file")

f = open(file, 'r')
for line in f:
    mf = open(newfilename, 'a')
    
    # Do the Shodan thing here
    # Wrap the request in a try/ except block to catch errors
    try:
        # Search Shodan
        query = "net:"+ "\"" + line.rstrip() + "\"" 
        mf.write("***********************************************************\n")
        mf.write("Performing a query on " + query + "\n")
        mf.write("***********************************************************\n")
        results = api.search(query)
        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                mf.write('IP: {}'.format(result['ip_str']) + "\n")
                mf.write('Port: {}'.format(result['port']) + "\n")
                mf.write(result['data'] + "\n")
                mf.write("   \n")
        time.sleep(1) #need this to make the API happy.. too fast and it complains
    except shodan.APIError as e:
        print('Error: {}'.format(e))

    mf.close()
