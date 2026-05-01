//==================================Local Storage====================================//
/*
    Store in browser
    ** Clear data manually
    Data store in key value pair
    Data stoage max size 5mb
    Browser and site specific
    Show in browser
 */
// Set Local Storage
localStorage.setItem('name', 'arijit')

// Get Local Storage
localStorage.getItem('name')

// Remove Local Storage
localStorage.removeItem('name')

// Clear Local Storage
localStorage.clear()

//==========================Session Storage==================================//
/*
    Store in browser
    ** Clear when browser close
    Data store in key value pair
    Data stoage max size 5mb
    Browser and site specific
    Show in browser
 */

// Set Session Storage
sessionStorage.setItem('name', 'arijit')

// Get Session Storage
sessionStorage.getItem('name')

// Remove Session Storage
sessionStorage.removeItem('name')

// Clear Session Storage
sessionStorage.clear()

//==========================Cookies Storage==================================//
/*
    Store in browser
    ** Expire date when cookie create
    Data store in key value pair
    Data stoage small data size 4kb
    Show in browser
    store in client and server side, mostly in server side
 */

// Set Cookie Storage
document.cookie = 'name=arijit; expire=Fri, 31st Dec 2026 23:59:59 GMT; path=/'

