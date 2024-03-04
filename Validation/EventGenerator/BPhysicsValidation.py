import FWCore.ParameterSet.Config as cms

def BPhysicsValidation(**kwargs):
  mod = cms.EDProducer('BPhysicsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
