import FWCore.ParameterSet.Config as cms

def PUGenParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('PUGenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
