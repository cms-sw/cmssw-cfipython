import FWCore.ParameterSet.Config as cms

def PATGenericParticleSelector(*args, **kwargs):
  mod = cms.EDFilter('PATGenericParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
