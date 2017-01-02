import 'package:serial_port/serial_port.dart';
import 'dart:async';

main() async {
  var arduino = new SerialPort("/dev/tty.usbmodem1421");
  arduino.onRead.map(BYTES_TO_STRING).listen(print);
  await arduino.open();
  // Wait a little bit before sending data
  new Timer(new Duration(seconds: 2), () => arduino.writeString("Hello !"));
}