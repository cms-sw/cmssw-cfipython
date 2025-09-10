import FWCore.ParameterSet.Config as cms

def RPCDigiValid(*args, **kwargs):
  mod = cms.EDProducer('RPCDigiValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
