import FWCore.ParameterSet.Config as cms

def ThresholdAbortAllocMonitor(*args, **kwargs):
  mod = cms.Service('ThresholdAbortAllocMonitor',
    skipCount = cms.untracked.uint32(0),
    minThreshold = cms.required.untracked.uint64,
    maxThreshold = cms.untracked.uint64(0)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
