# State Server Assignment

## Simple server
To start I have built a simple server for determining state. It uses a barebones django server to make setup and execution quick.
It uses the supplied states.json and a package called shapely to construct a point object with the given longitude and latitude.
It then loops over the states, constructing a polygon using the border coordinates for each, after which it checks if the point is in the polygon.

To run:
```
chmod +x ./state_server
./state_server &
```

## Advanced server
After that i have built a similar server with more advanced matching using US Cartographic Boundary Files. These files each contain more detailed boundary coordinates which allows for a more precise matching.

To run:
```
chmod +x ./advanced_state_server
./advanced_state_server
```

## Expected Behavior

  $ ./state-server &
  [1] 21507
  $ curl  -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/
  ["Pennsylvania"]
  $


## Notes

Given that file, it took one of us about an hour to implement something that
worked correctly. You're welcome to take it however far you want, but we're
expecting something along those lines.

And if there's anything special we have to do to run your program, just let us
know. A Makefile never hurt anyone.
