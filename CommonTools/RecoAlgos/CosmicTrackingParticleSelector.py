import FWCore.ParameterSet.Config as cms

def CosmicTrackingParticleSelector(**kwargs):
  mod = cms.EDFilter('CosmicTrackingParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
