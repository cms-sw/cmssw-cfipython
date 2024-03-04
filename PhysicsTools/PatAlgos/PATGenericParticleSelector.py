import FWCore.ParameterSet.Config as cms

def PATGenericParticleSelector(**kwargs):
  mod = cms.EDFilter('PATGenericParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
