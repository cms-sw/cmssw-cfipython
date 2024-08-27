import FWCore.ParameterSet.Config as cms

def MCSmartSingleParticleFilter(**kwargs):
  mod = cms.EDFilter('MCSmartSingleParticleFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
