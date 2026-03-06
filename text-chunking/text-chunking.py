def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    if len(tokens) == 0:
        return []
    chunks = []
    if len(tokens) < chunk_size:
        chunks.append(tokens) 
    step = chunk_size - overlap
    # if len(tokens) < step && tokens not in :
    #     return tokens[0:len(tokens)]
    # return [tokens[0:chunk_size]] + text_chunking(tokens[step:],chunk_size,overlap)
    for i in range(0, len(tokens),step):
        
        
        # del(tokens[0:step])
        # if len(chunks) == math.ceil(len(tokens)/chunk_size):
        #     break
        # if chunks[len(chunks)-1] == tokens[len(tokens)-1]:
        #     break
        chunk = tokens[i:i+chunk_size]
        if i+chunk_size > len(tokens):
            break
        chunks.append(chunk)
    
    return chunks
    
            
    
    
        
    