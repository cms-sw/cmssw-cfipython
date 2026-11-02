import FWCore.ParameterSet.Config as cms

def ONNXService(*args, **kwargs):
  mod = cms.Service('ONNXService',
    verbose = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
