import FWCore.ParameterSet.Config as cms

def ONNXService(*args, **kwargs):
  mod = cms.Service('ONNXService',
    allowTF32 = cms.bool(False),
    verbose = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
