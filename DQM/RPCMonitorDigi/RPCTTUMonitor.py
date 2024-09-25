import FWCore.ParameterSet.Config as cms

def RPCTTUMonitor(*args, **kwargs):
  mod = cms.EDProducer('RPCTTUMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
