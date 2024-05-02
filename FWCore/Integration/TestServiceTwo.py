import FWCore.ParameterSet.Config as cms

def TestServiceTwo(**kwargs):
  mod = cms.Service('TestServiceTwo',
    verbose = cms.untracked.bool(False),
    printTimestamps = cms.untracked.bool(False)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
