import FWCore.ParameterSet.Config as cms

def RPCTwinMuxRawToDigi(**kwargs):
  mod = cms.EDProducer('RPCTwinMuxRawToDigi',
    inputTag = cms.InputTag('rawDataCollector'),
    calculateCRC = cms.bool(True),
    fillCounters = cms.bool(True),
    bxMin = cms.int32(-2),
    bxMax = cms.int32(2),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
