import FWCore.ParameterSet.Config as cms

def PATPackedGenParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPackedGenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
