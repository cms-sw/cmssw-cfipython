import FWCore.ParameterSet.Config as cms

def RPCTechnicalTrigger(**kwargs):
  mod = cms.EDProducer('RPCTechnicalTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
