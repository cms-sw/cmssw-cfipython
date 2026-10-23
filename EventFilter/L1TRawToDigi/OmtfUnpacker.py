import FWCore.ParameterSet.Config as cms

def OmtfUnpacker(*args, **kwargs):
  mod = cms.EDProducer('OmtfUnpacker',
    inputLabel = cms.InputTag('rawDataCollector'),
    skipRpc = cms.bool(False),
    skipCsc = cms.bool(False),
    skipDt = cms.bool(False),
    skipMuon = cms.bool(False),
    useRpcConnectionFile = cms.bool(False),
    rpcConnectionFile = cms.string(''),
    outputTag = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
