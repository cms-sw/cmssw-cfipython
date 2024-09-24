import FWCore.ParameterSet.Config as cms

def PATGenericParticleRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATGenericParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
