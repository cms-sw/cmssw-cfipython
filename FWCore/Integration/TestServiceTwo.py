import FWCore.ParameterSet.Config as cms

def TestServiceTwo(*args, **kwargs):
  mod = cms.Service('TestServiceTwo',
    verbose = cms.untracked.bool(False),
    printTimestamps = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
