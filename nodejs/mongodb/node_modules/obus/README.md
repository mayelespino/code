#obus [![Build Status](https://travis-ci.org/fistlabs/obus.svg?branch=master)](https://travis-ci.org/fistlabs/obus)

```obus``` is deep object accessor

##Usage
```js
var Obus = require('obus');
var obus = new Obus();

obus.set('a.b.c', 42);
```

##API

###```Obus new Obus()```
Creates new ```Obus``` object

```js
var obus = new Obus();
```

###```* obus.set(String path, * data)```
Puts the given object deep into object according to given path

```js
var obus = new Obus();
obus.set('a.b.c', 42);
obus.valueOf(); // -> {a: {b: {c: 42}}}
```

###```* obus.get(String path[, * defaultValue])```
Returns the value placed deep in object according to given path. Returns the second argument if returning value is ```undefined```

```js
var obus = new Obus();
obus.set('a.b.c', 42);

obus.get('a.b'); // -> {c: 42}
obus.get('a.b.c'); // -> 42
obus.get('a.b.c.d'); // -> undefined
obus.get('a.b.c.d', 146); // -> 146
```

###```Boolean obus.del(String path)```
Deletes data from given path. Returns true if the data was deleted else false
```js
var obus = new Obus();
obus.set('a', 42);

obus.del('a'); // -> true
obus.del('a'); // -> false
```

###```Boolean obus.has(String path)```
Checks if any truey (not ```undefined```) data placed by the given path
```js
var obus = new Obus();
obus.set('a.b', 42);

obus.has('a.b'); // -> true
obus.has('a'); // -> true
obus.has('a.b.c'); // -> false
```

###```* obus.add(String path, * data)```
Extends existing data with the given value
```js
var obus = new Obus();
obus.set('a.b', 42);

obus.add('a', {c: 42});
obus.valueOf(); // -> {a: {b: 42, c: 42}}
```

##Also
You can use brace accesors if the properties you want is not identifiers.
```js
var obus = new Obus();

obus.set('foo.bar-baz', 42);  // error
//  string literals
obus.set('foo["bar-baz"]', 42); // done
obus.set("foo['bar-baz']", 42); // done
//  number literals
obus.set('foo[42]', 146); //  done

```
##License
[MIT](LICENSE)
