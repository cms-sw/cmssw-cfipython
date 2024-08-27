import FWCore.ParameterSet.Config as cms

def GenParticleCustomSelector(**kwargs):
  mod = cms.EDFilter('GenParticleCustomSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
