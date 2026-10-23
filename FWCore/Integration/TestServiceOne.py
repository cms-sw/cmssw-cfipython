import FWCore.ParameterSet.Config as cms

def TestServiceOne(*args, **kwargs):
  mod = cms.Service('TestServiceOne',
    verbose = cms.untracked.bool(False),
    printTimestamps = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
