# StartStopHelper
---------

Help admin to start / stop / restart the server

For permission level = `admin`

`!!start`: start the server

`!!stop [<time_wait>]`: stop the server

`!!restart [<time_wait>]`: restart the server

`!!stop_exit [<time_wait>]`: stop the server and exit MCDR

`!!exit`: exit MCDR

`[<time_wait>]` is an optional argument. if not set it's value is `10`. MCDR will count down for `time_wait` second to execute the command

For reducing `!!help` message and since normal player won't use this command I didn't add help message
