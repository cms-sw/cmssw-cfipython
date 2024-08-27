import FWCore.ParameterSet.Config as cms

def RPCFakeEvent(**kwargs):
  mod = cms.EDProducer('RPCFakeEvent',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
