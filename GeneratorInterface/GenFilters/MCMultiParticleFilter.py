import FWCore.ParameterSet.Config as cms

def MCMultiParticleFilter(**kwargs):
  mod = cms.EDFilter('MCMultiParticleFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
