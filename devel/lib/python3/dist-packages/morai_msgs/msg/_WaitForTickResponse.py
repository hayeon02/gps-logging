# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from morai_msgs/WaitForTickResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import morai_msgs.msg
import std_msgs.msg

class WaitForTickResponse(genpy.Message):
  _md5sum = "1c80ca1ddc5a285c8be87fef734111b0"
  _type = "morai_msgs/WaitForTickResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """bool tick_status
bool pause_status
uint64 frame

EgoVehicleStatus vehicle_status
string time

================================================================================
MSG: morai_msgs/EgoVehicleStatus
Header header
int32 unique_id
geometry_msgs/Vector3 acceleration
geometry_msgs/Vector3 position
geometry_msgs/Vector3 velocity

float64 heading
float32 accel
float32 brake
float32 wheel_angle

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['tick_status','pause_status','frame','vehicle_status','time']
  _slot_types = ['bool','bool','uint64','morai_msgs/EgoVehicleStatus','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       tick_status,pause_status,frame,vehicle_status,time

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(WaitForTickResponse, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.tick_status is None:
        self.tick_status = False
      if self.pause_status is None:
        self.pause_status = False
      if self.frame is None:
        self.frame = 0
      if self.vehicle_status is None:
        self.vehicle_status = morai_msgs.msg.EgoVehicleStatus()
      if self.time is None:
        self.time = ''
    else:
      self.tick_status = False
      self.pause_status = False
      self.frame = 0
      self.vehicle_status = morai_msgs.msg.EgoVehicleStatus()
      self.time = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_2BQ3I().pack(_x.tick_status, _x.pause_status, _x.frame, _x.vehicle_status.header.seq, _x.vehicle_status.header.stamp.secs, _x.vehicle_status.header.stamp.nsecs))
      _x = self.vehicle_status.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i10d3f().pack(_x.vehicle_status.unique_id, _x.vehicle_status.acceleration.x, _x.vehicle_status.acceleration.y, _x.vehicle_status.acceleration.z, _x.vehicle_status.position.x, _x.vehicle_status.position.y, _x.vehicle_status.position.z, _x.vehicle_status.velocity.x, _x.vehicle_status.velocity.y, _x.vehicle_status.velocity.z, _x.vehicle_status.heading, _x.vehicle_status.accel, _x.vehicle_status.brake, _x.vehicle_status.wheel_angle))
      _x = self.time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.vehicle_status is None:
        self.vehicle_status = morai_msgs.msg.EgoVehicleStatus()
      end = 0
      _x = self
      start = end
      end += 22
      (_x.tick_status, _x.pause_status, _x.frame, _x.vehicle_status.header.seq, _x.vehicle_status.header.stamp.secs, _x.vehicle_status.header.stamp.nsecs,) = _get_struct_2BQ3I().unpack(str[start:end])
      self.tick_status = bool(self.tick_status)
      self.pause_status = bool(self.pause_status)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.vehicle_status.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.vehicle_status.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 96
      (_x.vehicle_status.unique_id, _x.vehicle_status.acceleration.x, _x.vehicle_status.acceleration.y, _x.vehicle_status.acceleration.z, _x.vehicle_status.position.x, _x.vehicle_status.position.y, _x.vehicle_status.position.z, _x.vehicle_status.velocity.x, _x.vehicle_status.velocity.y, _x.vehicle_status.velocity.z, _x.vehicle_status.heading, _x.vehicle_status.accel, _x.vehicle_status.brake, _x.vehicle_status.wheel_angle,) = _get_struct_i10d3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.time = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_2BQ3I().pack(_x.tick_status, _x.pause_status, _x.frame, _x.vehicle_status.header.seq, _x.vehicle_status.header.stamp.secs, _x.vehicle_status.header.stamp.nsecs))
      _x = self.vehicle_status.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_i10d3f().pack(_x.vehicle_status.unique_id, _x.vehicle_status.acceleration.x, _x.vehicle_status.acceleration.y, _x.vehicle_status.acceleration.z, _x.vehicle_status.position.x, _x.vehicle_status.position.y, _x.vehicle_status.position.z, _x.vehicle_status.velocity.x, _x.vehicle_status.velocity.y, _x.vehicle_status.velocity.z, _x.vehicle_status.heading, _x.vehicle_status.accel, _x.vehicle_status.brake, _x.vehicle_status.wheel_angle))
      _x = self.time
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.vehicle_status is None:
        self.vehicle_status = morai_msgs.msg.EgoVehicleStatus()
      end = 0
      _x = self
      start = end
      end += 22
      (_x.tick_status, _x.pause_status, _x.frame, _x.vehicle_status.header.seq, _x.vehicle_status.header.stamp.secs, _x.vehicle_status.header.stamp.nsecs,) = _get_struct_2BQ3I().unpack(str[start:end])
      self.tick_status = bool(self.tick_status)
      self.pause_status = bool(self.pause_status)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.vehicle_status.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.vehicle_status.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 96
      (_x.vehicle_status.unique_id, _x.vehicle_status.acceleration.x, _x.vehicle_status.acceleration.y, _x.vehicle_status.acceleration.z, _x.vehicle_status.position.x, _x.vehicle_status.position.y, _x.vehicle_status.position.z, _x.vehicle_status.velocity.x, _x.vehicle_status.velocity.y, _x.vehicle_status.velocity.z, _x.vehicle_status.heading, _x.vehicle_status.accel, _x.vehicle_status.brake, _x.vehicle_status.wheel_angle,) = _get_struct_i10d3f().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.time = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.time = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2BQ3I = None
def _get_struct_2BQ3I():
    global _struct_2BQ3I
    if _struct_2BQ3I is None:
        _struct_2BQ3I = struct.Struct("<2BQ3I")
    return _struct_2BQ3I
_struct_i10d3f = None
def _get_struct_i10d3f():
    global _struct_i10d3f
    if _struct_i10d3f is None:
        _struct_i10d3f = struct.Struct("<i10d3f")
    return _struct_i10d3f
