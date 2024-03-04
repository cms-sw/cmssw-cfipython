import FWCore.ParameterSet.Config as cms

def GenParticleSelector(**kwargs):
  mod = cms.EDFilter('GenParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
