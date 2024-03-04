import FWCore.ParameterSet.Config as cms

def PATGenericParticleRefSelector(**kwargs):
  mod = cms.EDFilter('PATGenericParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
