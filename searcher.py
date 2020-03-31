from similitudeFunction import SimilitudeFunction

#class Searcher:


document = 'coche rojo guille madrid pablo coche cris guille mesa'
query = 'coche pablo'
sf = SimilitudeFunction()
result = sf.similitude(query, document, "scalarTF")


