import FWCore.ParameterSet.Config as cms

def OmtfPacker(**kwargs):
  mod = cms.EDProducer('OmtfPacker',
    rpcInputLabel = cms.InputTag(''),
    cscInputLabel = cms.InputTag(''),
    dtPhInputLabel = cms.InputTag(''),
    dtThInputLabel = cms.InputTag(''),
    skipRpc = cms.bool(False),
    skipCsc = cms.bool(False),
    skipDt = cms.bool(False),
    useRpcConnectionFile = cms.bool(False),
    rpcConnectionFile = cms.string(''),
    outputTag = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
