# python3
# idea from https://automatetheboringstuff.com/chapter11/
# opens Google maps with in the browser using an addressed pasted via clipboard or command line argument
# usage: 
#   mapme 870 Valencia St, San Francisco, CA 94110
#   mapme
# use command line arguments instead of clipboard if there is no agument the clipboard will be used
# Maps web site: i.e. https://www.google.com/maps/place/Parkring+29,+85748+Garching
# Maps web site: https://www.google.com/maps/place/<your-addr-atr>
# Maps web site: https://www.google.com/maps/place/Garching+85748+Parkring+29

import sys, webbrowser

# constant values
google_maps_url = 'http://maps.google.com/maps/place/'

if len(sys.argv) > 1:
   # Get address from command line.
   # you can do "print (sys.argv) variable to see all the information
   lookup_address = ' '.join(sys.argv[1:]) # with the join argument all information will be treated as one string
else:
   # get address from clipboard
   lookup_address = pyperclip.paste()
   
# Get address from cliboard
#  len(sys.argv) if > 1 then command line argument is available

webbrowser.open(google_maps_url + lookup_address)
