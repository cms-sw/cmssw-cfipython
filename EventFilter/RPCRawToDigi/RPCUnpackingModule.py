import FWCore.ParameterSet.Config as cms

def RPCUnpackingModule(*args, **kwargs):
  mod = cms.EDProducer('RPCUnpackingModule',
    InputLabel = cms.InputTag('rawDataCollector'),
    doSynchro = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
