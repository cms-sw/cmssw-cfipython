import FWCore.ParameterSet.Config as cms

def MultiParticleInConeGunProducer(*args, **kwargs):
  mod = cms.EDProducer('MultiParticleInConeGunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
