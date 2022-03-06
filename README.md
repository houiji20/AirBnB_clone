

# Description of the project

This is the first step towards building our first full web application: the AirBnB clone.
This first step is very important because we will use what we build during this project with all other following projects, in it we are going to write a command interpreter to manage our AirBnB objects:

    *  Create a new object(ex: a new User or a new Place)
    *  Retrieve an object from a file, a database etc…
    * Do operations on objects(count, compute stats, etc…)
    * Update attributes of an object
    * Destroy an object




Use  the command interpreter hbnb in an interactive mode:

`
./console.py
`
`
(hbnb)(command)
`


Use hbnb in non-interactive mode too by:

`echo "command" | ./console.py`

# How to Use Command Interpreter
---
| Commands | Sample Usage | Functionality |
| --------- | --------------------------------------------- | ------------------------------------------ |
| `help` | `help` | displays all commands available |
| `create` | `create < class >` | creates new object(ex. a new User, Place) |
| `update` | `User.update('123', {'name': 'Greg_n_Mel'})` | updates attribute of an object |
| `destroy` | `User.destroy('123')` | destroys specified object |
| `show` | `User.show('123')` | retrieve an object from a file, a database |
| `all` | `User.all()` | display all objects in class |
| `count` | `User.count()` | returns count of objects in specified class|
| `quit` | `quit` | exits |

# Usage
Interactive Mode
```
 ./console.py
(hbnb) help
Documented commands (type help < topic > ):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit

```
Non-Interactive Mode
```
 echo "help" | ./console.py
(hbnb)
Documented commands (type help < topic > ):
========================================
EOF  help  quit
(hbnb)

 cat test_help
help

 cat test_help | ./console.py
(hbnb)
Documented commands (type help < topic > ):
========================================
EOF  help  quit
(hbnb)

```

