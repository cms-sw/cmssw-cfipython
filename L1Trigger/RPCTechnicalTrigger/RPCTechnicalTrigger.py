import FWCore.ParameterSet.Config as cms

def RPCTechnicalTrigger(*args, **kwargs):
  mod = cms.EDProducer('RPCTechnicalTrigger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
