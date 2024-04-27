
"use strict";

let GetTrafficLightStatus = require('./GetTrafficLightStatus.js');
let Lamps = require('./Lamps.js');
let EgoVehicleStatus = require('./EgoVehicleStatus.js');
let VehicleSpecIndex = require('./VehicleSpecIndex.js');
let SensorPosControl = require('./SensorPosControl.js');
let VehicleSpec = require('./VehicleSpec.js');
let SyncModeSetGear = require('./SyncModeSetGear.js');
let SyncModeInfo = require('./SyncModeInfo.js');
let ERP42Info = require('./ERP42Info.js');
let MoraiSimProcStatus = require('./MoraiSimProcStatus.js');
let MoraiSrvResponse = require('./MoraiSrvResponse.js');
let GPSMessage = require('./GPSMessage.js');
let VehicleCollision = require('./VehicleCollision.js');
let RadarDetection = require('./RadarDetection.js');
let SyncModeCmd = require('./SyncModeCmd.js');
let ObjectStatus = require('./ObjectStatus.js');
let GhostMessage = require('./GhostMessage.js');
let ReplayInfo = require('./ReplayInfo.js');
let EgoDdVehicleStatus = require('./EgoDdVehicleStatus.js');
let PREvent = require('./PREvent.js');
let MapSpec = require('./MapSpec.js');
let SetTrafficLight = require('./SetTrafficLight.js');
let SyncModeCtrlCmd = require('./SyncModeCtrlCmd.js');
let SyncModeResultResponse = require('./SyncModeResultResponse.js');
let SyncModeRemoveObject = require('./SyncModeRemoveObject.js');
let MoraiTLInfo = require('./MoraiTLInfo.js');
let CtrlCmd = require('./CtrlCmd.js');
let EventInfo = require('./EventInfo.js');
let SyncModeScenarioLoad = require('./SyncModeScenarioLoad.js');
let VehicleCollisionData = require('./VehicleCollisionData.js');
let NpcGhostCmd = require('./NpcGhostCmd.js');
let IntersectionStatus = require('./IntersectionStatus.js');
let TrafficLight = require('./TrafficLight.js');
let IntscnTL = require('./IntscnTL.js');
let WaitForTickResponse = require('./WaitForTickResponse.js');
let NpcGhostInfo = require('./NpcGhostInfo.js');
let SaveSensorData = require('./SaveSensorData.js');
let SyncModeAddObject = require('./SyncModeAddObject.js');
let MultiEgoSetting = require('./MultiEgoSetting.js');
let IntersectionControl = require('./IntersectionControl.js');
let RadarDetections = require('./RadarDetections.js');
let WaitForTick = require('./WaitForTick.js');
let PRCtrlCmd = require('./PRCtrlCmd.js');
let CollisionData = require('./CollisionData.js');
let MapSpecIndex = require('./MapSpecIndex.js');
let ScenarioLoad = require('./ScenarioLoad.js');
let ObjectStatusList = require('./ObjectStatusList.js');
let SyncModeCmdResponse = require('./SyncModeCmdResponse.js');
let DdCtrlCmd = require('./DdCtrlCmd.js');
let MoraiSimProcHandle = require('./MoraiSimProcHandle.js');
let PRStatus = require('./PRStatus.js');
let MoraiTLIndex = require('./MoraiTLIndex.js');

module.exports = {
  GetTrafficLightStatus: GetTrafficLightStatus,
  Lamps: Lamps,
  EgoVehicleStatus: EgoVehicleStatus,
  VehicleSpecIndex: VehicleSpecIndex,
  SensorPosControl: SensorPosControl,
  VehicleSpec: VehicleSpec,
  SyncModeSetGear: SyncModeSetGear,
  SyncModeInfo: SyncModeInfo,
  ERP42Info: ERP42Info,
  MoraiSimProcStatus: MoraiSimProcStatus,
  MoraiSrvResponse: MoraiSrvResponse,
  GPSMessage: GPSMessage,
  VehicleCollision: VehicleCollision,
  RadarDetection: RadarDetection,
  SyncModeCmd: SyncModeCmd,
  ObjectStatus: ObjectStatus,
  GhostMessage: GhostMessage,
  ReplayInfo: ReplayInfo,
  EgoDdVehicleStatus: EgoDdVehicleStatus,
  PREvent: PREvent,
  MapSpec: MapSpec,
  SetTrafficLight: SetTrafficLight,
  SyncModeCtrlCmd: SyncModeCtrlCmd,
  SyncModeResultResponse: SyncModeResultResponse,
  SyncModeRemoveObject: SyncModeRemoveObject,
  MoraiTLInfo: MoraiTLInfo,
  CtrlCmd: CtrlCmd,
  EventInfo: EventInfo,
  SyncModeScenarioLoad: SyncModeScenarioLoad,
  VehicleCollisionData: VehicleCollisionData,
  NpcGhostCmd: NpcGhostCmd,
  IntersectionStatus: IntersectionStatus,
  TrafficLight: TrafficLight,
  IntscnTL: IntscnTL,
  WaitForTickResponse: WaitForTickResponse,
  NpcGhostInfo: NpcGhostInfo,
  SaveSensorData: SaveSensorData,
  SyncModeAddObject: SyncModeAddObject,
  MultiEgoSetting: MultiEgoSetting,
  IntersectionControl: IntersectionControl,
  RadarDetections: RadarDetections,
  WaitForTick: WaitForTick,
  PRCtrlCmd: PRCtrlCmd,
  CollisionData: CollisionData,
  MapSpecIndex: MapSpecIndex,
  ScenarioLoad: ScenarioLoad,
  ObjectStatusList: ObjectStatusList,
  SyncModeCmdResponse: SyncModeCmdResponse,
  DdCtrlCmd: DdCtrlCmd,
  MoraiSimProcHandle: MoraiSimProcHandle,
  PRStatus: PRStatus,
  MoraiTLIndex: MoraiTLIndex,
};
