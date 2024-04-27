// Generated by gencpp from file morai_msgs/MoraiSyncModeRemoveObjectSrv.msg
// DO NOT EDIT!


#ifndef MORAI_MSGS_MESSAGE_MORAISYNCMODEREMOVEOBJECTSRV_H
#define MORAI_MSGS_MESSAGE_MORAISYNCMODEREMOVEOBJECTSRV_H

#include <ros/service_traits.h>


#include <morai_msgs/MoraiSyncModeRemoveObjectSrvRequest.h>
#include <morai_msgs/MoraiSyncModeRemoveObjectSrvResponse.h>


namespace morai_msgs
{

struct MoraiSyncModeRemoveObjectSrv
{

typedef MoraiSyncModeRemoveObjectSrvRequest Request;
typedef MoraiSyncModeRemoveObjectSrvResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct MoraiSyncModeRemoveObjectSrv
} // namespace morai_msgs


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrv > {
  static const char* value()
  {
    return "d499baec7083a3731b7e7fc183807dce";
  }

  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrv&) { return value(); }
};

template<>
struct DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrv > {
  static const char* value()
  {
    return "morai_msgs/MoraiSyncModeRemoveObjectSrv";
  }

  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrv&) { return value(); }
};


// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest> should match
// service_traits::DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >
template<>
struct DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrvRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse> should match
// service_traits::MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >
template<>
struct MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse>
{
  static const char* value()
  {
    return MD5Sum< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse> should match
// service_traits::DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >
template<>
struct DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse>
{
  static const char* value()
  {
    return DataType< ::morai_msgs::MoraiSyncModeRemoveObjectSrv >::value();
  }
  static const char* value(const ::morai_msgs::MoraiSyncModeRemoveObjectSrvResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // MORAI_MSGS_MESSAGE_MORAISYNCMODEREMOVEOBJECTSRV_H
