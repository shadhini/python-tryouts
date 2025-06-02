# Generators
* used to create iterators, but with a different approach. 

`Generators` are 
* simple `functions` which `return` 
  * an iterable set of items, 
  * one at a time, 
  * in a special way.

* When an iteration over a set of item starts using the `for` statement, the `generator is run`. 
* Once the generator's function code reaches a `"yield"` statement, the `generator yields` its execution back `to the for loop`, returning a new value from the set. 
* The generator function can generate as many values `(possibly infinite)` as it wants, yielding each one in its turn.