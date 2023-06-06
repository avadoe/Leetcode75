import string

def suggestedProducts(products, searchWord):
    idx = 0
    
    ans = []
    
    while idx < len(searchWord):
        curr_string = searchWord[:idx + 1]
        
        present_list = []
        for product in products: 
            if product.startswith(curr_string):
                present_list.append(product)
                
            present_list.sort()
            present_list = present_list[:3]
                
        ans.append(present_list)
        idx += 1
        
    return ans

print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))