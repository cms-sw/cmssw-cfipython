import FWCore.ParameterSet.Config as cms

def PresentThresholdAbortAllocMonitor(*args, **kwargs):
  mod = cms.Service('PresentThresholdAbortAllocMonitor',
    skipCount = cms.untracked.uint32(0),
    threshold = cms.required.untracked.uint64
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
