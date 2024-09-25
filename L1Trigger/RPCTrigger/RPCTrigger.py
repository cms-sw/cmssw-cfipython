import FWCore.ParameterSet.Config as cms

def RPCTrigger(*args, **kwargs):
  mod = cms.EDProducer('RPCTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
