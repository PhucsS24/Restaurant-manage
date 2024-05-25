var updatebtns = document.getElementsByClassName('update-cart')

for (i=0; i< updatebtns.length; i++){
    updatebtns[i].addEventListener('click', function() {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('prodctId ',productId, 'action ', action)
        console.log('user ', user)
        if (user === "AnonymousUser") {
            console.log("user not login")
        } else {
            console.log("user logged in, success add item.")
        }
    })
}