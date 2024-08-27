import FWCore.ParameterSet.Config as cms

def TrackingParticleRefSelector(**kwargs):
  mod = cms.EDFilter('TrackingParticleRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
