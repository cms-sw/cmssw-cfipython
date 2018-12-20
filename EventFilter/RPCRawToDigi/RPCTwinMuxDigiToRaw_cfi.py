import FWCore.ParameterSet.Config as cms

RPCTwinMuxDigiToRaw = cms.EDProducer('RPCTwinMuxDigiToRaw',
  inputTag = cms.InputTag('simMuonRPCDigis'),
  bxMin = cms.int32(-2),
  bxMax = cms.int32(2),
  ignoreEOD = cms.bool(True),
  eventType = cms.int32(1),
  uFOV = cms.uint32(1)
)
