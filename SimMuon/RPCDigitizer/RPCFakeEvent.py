import FWCore.ParameterSet.Config as cms

def RPCFakeEvent(*args, **kwargs):
  mod = cms.EDProducer('RPCFakeEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
