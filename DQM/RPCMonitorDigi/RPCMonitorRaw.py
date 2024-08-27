import FWCore.ParameterSet.Config as cms

def RPCMonitorRaw(**kwargs):
  mod = cms.EDProducer('RPCMonitorRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
