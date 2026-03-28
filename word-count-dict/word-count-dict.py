def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    empty_dict_braces = {}

    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            
            if sentences[i][j] in empty_dict_braces:
                
                empty_dict_braces[sentences[i][j]]+=1
            else:
                
                empty_dict_braces[sentences[i][j]]=1

    return empty_dict_braces
                
                
    
    pass