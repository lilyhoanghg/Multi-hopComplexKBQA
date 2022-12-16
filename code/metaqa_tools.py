# regular expression for entity id in Wikimovies RDF e.g. movie123, entity456
wikimovies_entity_re = '^[a-z]+[0-9]+'
freebase_entity_re = '^[mg]\.'

def is_wm_entity_name(name):
    '''
    Given a name, check if it follows entity name convention of Wikimovies RDF.
    '''
    if re.search(wikimovies_entity_re, name):
        return True
    else:
        return False

def is_freebase_entity_name(name):
    if re.search(freebase_entity_re, name):
        return True
    else:
        return False