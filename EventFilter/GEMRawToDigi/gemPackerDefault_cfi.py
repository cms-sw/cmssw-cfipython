import FWCore.ParameterSet.Config as cms

gemPackerDefault = cms.EDProducer('GEMDigiToRawModule',
  gemDigi = cms.InputTag('simMuonGEMDigis'),
  eventType = cms.int32(0),
  useDBEMap = cms.bool(False)
)
