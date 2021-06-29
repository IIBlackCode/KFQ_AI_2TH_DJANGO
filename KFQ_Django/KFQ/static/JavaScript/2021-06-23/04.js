const article = {
    num: 1,
    title: 'A',
    reply: [
        { num: 3, title: 'A-3' },
        { num: 2, title: 'A-2' },
        { num: 1, title: 'A-1' }
    ]
};

for(let key in article) {
    console.log('typeof(article[key]) :',typeof(article[key]));
    if (typeof(article[key]) == 'object') {
        for(let value of article[key]){
            console.log(value);
        }
    }else{
        console.log(key, article[key]);
    }
}