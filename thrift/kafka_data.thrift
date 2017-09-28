namespace py kafka_data

struct Kafka_Data {
   1: string type,
   2: string contact,
   3: string message
}

exception InvalidValueException {
  1: i32 error_code,
  2: string error_msg
}