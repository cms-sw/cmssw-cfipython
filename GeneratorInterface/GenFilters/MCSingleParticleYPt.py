import FWCore.ParameterSet.Config as cms

def MCSingleParticleYPt(*args, **kwargs):
  mod = cms.EDFilter('MCSingleParticleYPt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
