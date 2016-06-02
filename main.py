import csv
import logging
import datetime
from urllib.request import urlopen
from urllib.parse import quote_plus

def ReadSymbol(symbol):
    max_open = 0.0
    min_open = float('inf')
    max_close = 0.0
    min_close = float ('inf')
    max_high = 0.0
    min_high = float('inf')
    max_low = 0.0
    min_low = float ('inf')
    
    
    start = datetime.date(2015, 1, 1)
    end = datetime.date(2015, 12, 31)
    url = "http://www.google.com/finance/historical?q={0}&startdate={1}&enddate={2}&output=csv"
    url = url.format(symbol.upper(), quote_plus(start.strftime('%b %d, %Y')), quote_plus(end.strftime('%b %d, %Y')))
    data = urlopen(url).readlines()
    
    for line in data[1:]:
        values =  line.decode().strip().split(',')
        
        x = float(values[1])
        if x > max_open:
            max_open = x
        if x < min_open:
            min_open = x
            
        y = float(values[4])
        if y > max_close:
            max_close = y
        if y < min_close:
            min_close = y

        z = float(values[2])
        if z > max_high:
            max_high = z
        if z < min_high:
            min_high = z
            
        w = float(values[3])
        if w > max_low:
            max_low = w
        if w < min_low:
           min_low = w
            
            
   
    logging.info('max_open: ' + repr(max_open) + '  min_open: ' + repr(min_open))
    logging.info('max_close: ' + repr(max_close) + '  min_close: ' + repr(min_close))
    logging.info('max_high: ' + repr(max_high) + '  min_high: ' + repr(min_high))
    logging.info('max_low: ' + repr(max_low) + '  min_low: ' + repr(min_low))
    
        
 
 
def ReadFile(filename):
    max_open = 0.0
    min_open = float('inf')
    max_close = 0.0
    min_close = float ('inf')
    max_high = 0.0
    min_high = float('inf')
    max_low = 0.0
    min_low = float ('inf')
    
    with open(filename, 'r') as file:
        reader=csv.DictReader(file)
        for line in reader:
            x = float(line['Open'])
            if x > max_open:
                max_open = x
            if x < min_open:
                min_open = x
                
            y = float(line['Close'])
            if y > max_close:
                max_close = y
            if y < min_close:
                min_close = y

            z = float(line['High'])
            if z > max_high:
                max_high = z
            if z < min_high:
                min_high = z
                
            w = float(line['Low'])
            if w > max_low:
                max_low = w
            if w < min_low:
               min_low = w
            
            
   
    logging.info('max_open: ' + repr(max_open) + '  min_open: ' + repr(min_open))
    logging.info('max_close: ' + repr(max_close) + '  min_close: ' + repr(min_close))
    logging.info('max_high: ' + repr(max_high) + '  min_high: ' + repr(min_high))
    logging.info('max_low: ' + repr(max_low) + '  min_low: ' + repr(min_low))
    
if __name__ == '__main__':
    logging.basicConfig(filename='app.log', level=logging.INFO)
    try:
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", help="input filename")
        parser.add_argument("--symbol", help="stock symbol")
        args = parser.parse_args()
        
        
        logging.info('Welcome!')
        if args.file:
            ReadFile(args.file)
        elif args.symbol:
            ReadSymbol(args.symbol)
    except Exception:
        logging.info("error")
    

    
    
    
 
