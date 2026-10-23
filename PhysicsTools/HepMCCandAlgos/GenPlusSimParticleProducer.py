import FWCore.ParameterSet.Config as cms

def GenPlusSimParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('GenPlusSimParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
