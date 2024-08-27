import FWCore.ParameterSet.Config as cms

def ResourceEnforcer(**kwargs):
  mod = cms.Service('ResourceEnforcer',
    maxVSize = cms.untracked.double(0),
    maxRSS = cms.untracked.double(0),
    maxTime = cms.untracked.double(0)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
