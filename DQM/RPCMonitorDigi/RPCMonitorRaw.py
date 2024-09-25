import FWCore.ParameterSet.Config as cms

def RPCMonitorRaw(*args, **kwargs):
  mod = cms.EDProducer('RPCMonitorRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
