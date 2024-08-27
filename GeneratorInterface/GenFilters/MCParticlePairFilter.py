import FWCore.ParameterSet.Config as cms

def MCParticlePairFilter(**kwargs):
  mod = cms.EDFilter('MCParticlePairFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
