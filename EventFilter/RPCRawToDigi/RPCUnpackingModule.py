import FWCore.ParameterSet.Config as cms

def RPCUnpackingModule(**kwargs):
  mod = cms.EDProducer('RPCUnpackingModule',
    InputLabel = cms.InputTag('rawDataCollector'),
    doSynchro = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
