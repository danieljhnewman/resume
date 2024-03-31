fetch("https://xzsh4u3rj4ykvfa6jzcmispycu0mncqb.lambda-url.us-east-1.on.aws/").then( function(response) {
    return response.json()
    //✅data types:
    //1. json 
    //2. text 
    //3. blob 
    
}).then(function(result){
    //✅when promise is returned succesfully, response.data is logged inside result variable 
    document.getElementById("hitReturn").innerHTML = result.Item.hitcount.N;
    
}).catch(function(error){
    //✅when promise is failed 
    console.log(error)
})
/* testing github push*/