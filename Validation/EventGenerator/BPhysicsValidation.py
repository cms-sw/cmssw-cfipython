import FWCore.ParameterSet.Config as cms

def BPhysicsValidation(*args, **kwargs):
  mod = cms.EDProducer('BPhysicsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
