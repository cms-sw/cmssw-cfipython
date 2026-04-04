import FWCore.ParameterSet.Config as cms

def MCSmartSingleParticleFilter(*args, **kwargs):
  mod = cms.EDFilter('MCSmartSingleParticleFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
