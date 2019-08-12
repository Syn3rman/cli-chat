var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);

io.on('connection', function(socket){
    // console.log(socket, typeof socket);
    console.log("User connected");
    socket.on('message',(msg)=>{
        console.log('Message: ', msg);
    });
    socket.on('disconnect',()=>{
        console.log('User disconnected.');
    });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});