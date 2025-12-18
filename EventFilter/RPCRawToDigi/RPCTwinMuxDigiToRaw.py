import FWCore.ParameterSet.Config as cms

def RPCTwinMuxDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('RPCTwinMuxDigiToRaw',
    inputTag = cms.InputTag('simMuonRPCDigis'),
    bxMin = cms.int32(-2),
    bxMax = cms.int32(2),
    ignoreEOD = cms.bool(True),
    eventType = cms.int32(1),
    uFOV = cms.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
