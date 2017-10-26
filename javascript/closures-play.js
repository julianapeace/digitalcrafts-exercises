// This style of programming is called FUNCTIONAL PROGRAMMING.
function grandparent(inheritence){
  let b = 'Baby '
  function parent(inheritence){
    let a = 'Hey '
    function grandchild(inheritence){
      console.log(a+ b+'hello');
    }
    grandchild()
  }
  parent()
}

// inheritence = [1,2,3]

grandparent(123);
