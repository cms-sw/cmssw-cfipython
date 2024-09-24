import FWCore.ParameterSet.Config as cms

def ResourceEnforcer(*args, **kwargs):
  mod = cms.Service('ResourceEnforcer',
    maxVSize = cms.untracked.double(0),
    maxRSS = cms.untracked.double(0),
    maxTime = cms.untracked.double(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
