import FWCore.ParameterSet.Config as cms

def RPCTrigger(**kwargs):
  mod = cms.EDProducer('RPCTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
