import FWCore.ParameterSet.Config as cms

def MuonOffsetESProducer(**kwargs):
  mod = cms.ESProducer('MuonOffsetESProducer',
    fromDD4hep = cms.bool(False),
    names = cms.vstring(
      'MuonCommonNumbering',
      'MuonBarrel',
      'MuonEndcap',
      'MuonBarrelWheels',
      'MuonBarrelStation1',
      'MuonBarrelStation2',
      'MuonBarrelStation3',
      'MuonBarrelStation4',
      'MuonBarrelSuperLayer',
      'MuonBarrelLayer',
      'MuonBarrelWire',
      'MuonRpcPlane1I',
      'MuonRpcPlane1O',
      'MuonRpcPlane2I',
      'MuonRpcPlane2O',
      'MuonRpcPlane3S',
      'MuonRpcPlane4',
      'MuonRpcChamberLeft',
      'MuonRpcChamberMiddle',
      'MuonRpcChamberRight',
      'MuonRpcEndcap1',
      'MuonRpcEndcap2',
      'MuonRpcEndcap3',
      'MuonRpcEndcap4',
      'MuonRpcEndcapSector',
      'MuonRpcEndcapChamberB1',
      'MuonRpcEndcapChamberB2',
      'MuonRpcEndcapChamberB3',
      'MuonRpcEndcapChamberC1',
      'MuonRpcEndcapChamberC2',
      'MuonRpcEndcapChamberC3',
      'MuonRpcEndcapChamberE1',
      'MuonRpcEndcapChamberE2',
      'MuonRpcEndcapChamberE3',
      'MuonRpcEndcapChamberF1',
      'MuonRpcEndcapChamberF2',
      'MuonRpcEndcapChamberF3',
      'MuonEndcapStation1',
      'MuonEndcapStation2',
      'MuonEndcapStation3',
      'MuonEndcapStation4',
      'MuonEndcapSubrings',
      'MuonEndcapSectors',
      'MuonEndcapLayers',
      'MuonEndcapRing1',
      'MuonEndcapRing2',
      'MuonEndcapRing3',
      'MuonEndcapRingA',
      'MuonGEMEndcap',
      'MuonGEMSector',
      'MuonGEMChamber'
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
