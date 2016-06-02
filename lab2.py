import csv

def func():
    print(__name__)


if __name__ == '__main__':
    print('Welcome!')
    filename=input('Enter filename: ')
    
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
            
            
   
    print('max_open: ' + repr(max_open) + '  min_open: ' + repr(min_open))
    print('max_close: ' + repr(max_close) + '  min_close: ' + repr(min_close))
    print('max_high: ' + repr(max_high) + '  min_high: ' + repr(min_high))
    print('max_low: ' + repr(max_low) + '  min_low: ' + repr(min_low))
    
 
