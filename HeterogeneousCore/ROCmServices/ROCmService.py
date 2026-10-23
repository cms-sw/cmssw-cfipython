import FWCore.ParameterSet.Config as cms

def ROCmService(*args, **kwargs):
  mod = cms.Service('ROCmService',
    enabled = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    limits = cms.untracked.PSet(
      hipLimitStackSize = cms.untracked.int32(-1),
      hipLimitMallocHeapSize = cms.untracked.int32(-1)
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
