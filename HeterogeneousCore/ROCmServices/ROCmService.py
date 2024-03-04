import FWCore.ParameterSet.Config as cms

def ROCmService(**kwargs):
  mod = cms.Service('ROCmService',
    enabled = cms.untracked.bool(True),
    verbose = cms.untracked.bool(False),
    limits = cms.untracked.PSet(
      hipLimitStackSize = cms.untracked.int32(-1),
      hipLimitMallocHeapSize = cms.untracked.int32(-1)
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
