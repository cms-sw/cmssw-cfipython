import FWCore.ParameterSet.Config as cms

def MergedGenParticleProducer(*args, **kwargs):
  mod = cms.EDProducer('MergedGenParticleProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
