import FWCore.ParameterSet.Config as cms

def TrackingParticleSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackingParticleSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
