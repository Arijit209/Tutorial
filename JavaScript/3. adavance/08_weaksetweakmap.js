//============================================================Symbols====================================================//
// 1. Unique identifiers for object properties
const symbol1 = Symbol('id');
const symbol2 = Symbol('id');
console.log(symbol1 === symbol2); // false

// 2. Hidden properties
const user = {
    name: 'John',
};
const uid = Symbol('id');
user[uid] = 12345;
console.log(user);
console.log(Object.keys(user)); // ['name']

//=======================================================Weak Set=======================================================//
// Show the private data of an object without exposing it to the outside world. 
// WeakSet only accepts objects as values and does not prevent garbage collection of those objects.
const user1 = { name: 'Alice' };
const user2 = { name: 'Bob' };
const weakSet = new WeakSet();
weakSet.add(user1);
weakSet.add(user2);
console.log(weakSet.has(user1));

//=======================================================Weak Map=======================================================//
// Similar to WeakSet but stores key-value pairs. The keys must be objects, and the values can be of any type. 
// Like WeakSet, it does not prevent garbage collection of the keys.
const weakMap = new WeakMap();
const key1 = { id: 1 };
const key2 = { id: 2 }; 
weakMap.set(key1, 'Value for key1');
weakMap.set(key2, 'Value for key2');
console.log(weakMap.get(key1)); // 'Value for key1'