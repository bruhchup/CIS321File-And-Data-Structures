import Transcript

NICHOLASTSCRIPT = open('CSVParser/GPANicholas.csv', 'r')
HAYDENTSCRIPT = open('CSVParser/GPAHayden.csv', 'r')
    
def main():
    nichScript = Transcript.Transcript(NICHOLASTSCRIPT, 'Nicholas Moore')
    hayScript = Transcript.Transcript(HAYDENTSCRIPT, 'Hayden Banks')
    
    print(nichScript)
    print(hayScript)
    
if __name__ == '__main__':
    main()