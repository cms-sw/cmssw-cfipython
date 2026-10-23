import FWCore.ParameterSet.Config as cms

def MCParticlePairFilter(*args, **kwargs):
  mod = cms.EDFilter('MCParticlePairFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
