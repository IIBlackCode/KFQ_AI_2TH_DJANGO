const obj = {
    'pizza': '🍕',
    'chicken': '🍗',
    'meat': '🍖'
    };

for(key in obj){
    console.log('key:',key, '\t obj.key:',obj.key, '\t obj[key]:',obj[key]);
}