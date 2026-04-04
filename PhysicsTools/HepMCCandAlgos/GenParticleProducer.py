import FWCore.ParameterSet.Config as cms

def GenParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('GenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
