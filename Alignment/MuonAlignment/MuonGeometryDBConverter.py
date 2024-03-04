import FWCore.ParameterSet.Config as cms

def MuonGeometryDBConverter(**kwargs):
  mod = cms.EDAnalyzer('MuonGeometryDBConverter',
    input = cms.string('ideal'),
    dtLabel = cms.string(''),
    cscLabel = cms.string(''),
    gemLabel = cms.string(''),
    dtAPELabel = cms.string(''),
    cscAPELabel = cms.string(''),
    gemAPELabel = cms.string(''),
    shiftErr = cms.double(1000),
    angleErr = cms.double(6.28),
    getAPEs = cms.bool(True),
    output = cms.string('xml'),
    fileName = cms.string('REPLACEME.xml'),
    outputXML = cms.PSet(
      fileName = cms.string('REPLACEME.xml'),
      relativeto = cms.string('ideal'),
      rawIds = cms.bool(False),
      survey = cms.bool(False),
      eulerAngles = cms.bool(False),
      precision = cms.int32(10),
      suppressDTBarrel = cms.untracked.bool(True),
      suppressDTWheels = cms.untracked.bool(True),
      suppressDTStations = cms.untracked.bool(True),
      suppressDTChambers = cms.untracked.bool(False),
      suppressDTSuperLayers = cms.untracked.bool(False),
      suppressDTLayers = cms.untracked.bool(False),
      suppressCSCEndcaps = cms.untracked.bool(True),
      suppressCSCStations = cms.untracked.bool(True),
      suppressCSCRings = cms.untracked.bool(True),
      suppressCSCChambers = cms.untracked.bool(False),
      suppressCSCLayers = cms.untracked.bool(False),
      suppressGEMEndcaps = cms.untracked.bool(True),
      suppressGEMStations = cms.untracked.bool(True),
      suppressGEMRings = cms.untracked.bool(True),
      suppressGEMSuperChambers = cms.untracked.bool(False),
      suppressGEMChambers = cms.untracked.bool(True),
      suppressGEMEtaPartitions = cms.untracked.bool(True)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
