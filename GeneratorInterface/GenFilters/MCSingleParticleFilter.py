import FWCore.ParameterSet.Config as cms

def MCSingleParticleFilter(**kwargs):
  mod = cms.EDFilter('MCSingleParticleFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
