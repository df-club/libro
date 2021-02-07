var ros = new ROSLIB.Ros({
    url: 'ws://localhost:9090'
});

ros.on('connection', function () {
    $("#status span").text("CONNETCTED");
    $("#status span").css({ "color": "#999" });
});

ros.on('error', function (error) {
    $("#status span").text("Error connecting to websocket server:" + error);
    $("#status span").css({ "color": "#ff0000" });
});

ros.on('close', function () {
    $("#status span").text("Connection to websocket server closed.");
    $("#status span").css({ "color": "#ff0000" });
});

var speed = 0.1;
var turn = 1;
var cmdVel = new ROSLIB.Topic({
    ros: ros,
    name: '/cmd_vel',
    messageType: 'geometry_msgs/Twist'
});
var x = 0;
var th = 0;
var status = 0;
var count = 0;
var acc = 0.1;
var target_speed = 0;
var target_turn = 0;
var control_speed = 0;
var control_turn = 0;
function changeTwoDecimal_f(x) {
    var f_x = parseFloat(x);
    var f_x = Math.round(x * 10) / 10;
    var s_x = f_x.toString();
    var pos_decimal = s_x.indexOf('.');
    if (pos_decimal < 0) {
        pos_decimal = s_x.length;
        s_x += '.';
    }
    while (s_x.length <= pos_decimal + 1) {
        s_x += '0';
    }
    return s_x;
}
function isNum(val) {
    if (val === "" || val == null) {
        return false;
    }
    if (!isNaN(val)) {
        return true;
    }
    else {
        return false;
    }
}
$('.speed_x input').val(changeTwoDecimal_f(speed));
$('.speed_subtract').on("click", function (e) {
    if (speed >= 0.2) {
        speed = speed - 0.1;
        $('.speed_x input').val(changeTwoDecimal_f(speed));
    }
});
$('.speed_add').on("click", function (e) {
    speed = speed + 0.1;
    $('.speed_x input').val(changeTwoDecimal_f(speed));
});
$('.speed_x input').on("change", function (e) {
    if(isNum(parseFloat(e.target.value)) && parseFloat(e.target.value) >= 0.1){
            speed = parseFloat(e.target.value);
            $('.speed_x input').val(changeTwoDecimal_f(speed));
    }
    else{
        $('.speed_x input').val(changeTwoDecimal_f(speed));
    }
});

$('.theta input').val(changeTwoDecimal_f(turn));
$('.th_subtract').on("click", function (e) {
    if (turn >= 0.2) {
        turn = turn - 0.1;
        $('.theta input').val(changeTwoDecimal_f(turn));
    }
});
$('.th_add').on("click", function (e) {
    turn = turn + 0.1;
    $('.theta input').val(changeTwoDecimal_f(turn));
});
$('.theta input').on("change", function (e) {
    if(isNum(parseFloat(e.target.value)) && parseFloat(e.target.value) >= 0.1){
            turn = parseFloat(e.target.value);
            $('.theta input').val(changeTwoDecimal_f(turn));
    }
    else{
        $('.theta input').val(changeTwoDecimal_f(turn));
    }
});

function pubStopSmoothly() {
    x = 0;
    th = 0;
    control_speed = 0;
    control_turn = 0;
    pubTwist();
}
function pubForward() {
    x = 1;
    th = 0;
    pubTwist();
}
function pubBack() {
    x = -1;
    th = 0;
    pubTwist();
}
function pubLeft() {
    x = 0;
    th = 1;
    pubTwist();
}
function pubRight() {
    x = 0;
    th = -1;
    pubTwist();
}
function pubForwardLeft() {
    x = 1;
    th = 1;
    pubTwist();
}
function pubForwardRight() {
    x = 1;
    th = -1;
    pubTwist();
}
function pubBackLeft() {
    x = -1;
    th = -1;
    pubTwist();
}
function pubBackRight() {
    x = -1;
    th = 1;
    pubTwist();
}
function pubTwist() {
    target_speed = speed * x;
    target_turn = turn * th;
    if (target_speed > control_speed) {
        control_speed = Math.min(target_speed, control_speed + 0.02);
    }
    if (target_speed < control_speed) {
        control_speed = Math.max(target_speed, control_speed - 0.02);
    }
    if (target_speed == control_speed) {
        control_speed = target_speed;
    }


    if (target_turn > control_turn) {
        control_turn = Math.min(target_turn, control_turn + 0.1);
    }
    if (target_turn < control_turn) {
        control_turn = Math.max(target_turn, control_turn - 0.1);
    }
    if (target_turn == control_turn) {
        control_turn = target_turn;
    }
    var twist = new ROSLIB.Message({
        linear: {
            x: control_speed,
            y: 0,
            z: 0
        },
        angular: {
            x: 0,
            y: 0,
            z: control_turn
        }
    });
    cmdVel.publish(twist);
}

window.forwardTime;
window.backTime;
window.leftTime;
window.rightTime;
window.forwardLeftTime;
window.forwardRightTime;
window.backLeftTime;
window.backRightTime;

function clearAllTimer() {
    window.clearInterval(window.forwardTime);
    window.clearInterval(window.backTime);
    window.clearInterval(window.leftTime);
    window.clearInterval(window.rightTime);
    window.clearInterval(window.forwardLeftTime);
    window.clearInterval(window.forwardRightTime);
    window.clearInterval(window.backLeftTime);
    window.clearInterval(window.backRightTime);
}
$(document).ready(function () {
    $("#forward_btn").on("mousedown", function () {
        clearAllTimer();
        window.forwardTime = window.setInterval(pubForward, 100);
    });
    $("#back_btn").on("mousedown", function () {
        clearAllTimer();
        window.backTime = window.setInterval(pubBack, 100);
    });
    $("#left_btn").on("mousedown", function () {
        clearAllTimer();
        window.leftTime = window.setInterval(pubLeft, 100);
    });
    $("#right_btn").on("mousedown", function () {
        clearAllTimer();
        window.rightTime = window.setInterval(pubRight, 100);
    });
    $("#forwardLeft_btn").on("mousedown", function () {
        clearAllTimer();
        window.forwardLeftTime = window.setInterval(pubForwardLeft, 100);
    });
    $("#forwardRight_btn").on("mousedown", function () {
        clearAllTimer();
        window.forwardRightTime = window.setInterval(pubForwardRight, 100);
    });
    $("#backLeft_btn").on("mousedown", function () {
        clearAllTimer();
        window.backLeftTime = window.setInterval(pubBackLeft, 100);
    });
    $("#backRight_btn").on("mousedown", function () {
        clearAllTimer();
        window.backRightTime = window.setInterval(pubBackRight, 100);
    });
});
