import FWCore.ParameterSet.Config as cms

def GenParticleRefSelector(**kwargs):
  mod = cms.EDFilter('GenParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
