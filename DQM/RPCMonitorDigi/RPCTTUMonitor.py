import FWCore.ParameterSet.Config as cms

def RPCTTUMonitor(**kwargs):
  mod = cms.EDProducer('RPCTTUMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
