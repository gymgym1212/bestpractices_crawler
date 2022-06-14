
domain = "https://bestpractices.coreinfrastructure.org"
path = "/en/projects.csv"
max_pages = 158

for(let i=1;i<=max_pages;i++){
    fetch(domain+path+'?page='+i)
    .then(res => res.text)
    .then(data => {
        
    })
}