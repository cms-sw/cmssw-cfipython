import FWCore.ParameterSet.Config as cms

def CUDAMonitoringService(*args, **kwargs):
  mod = cms.Service('CUDAMonitoringService',
    memoryConstruction = cms.untracked.bool(False),
    memoryBeginStream = cms.untracked.bool(True),
    memoryPerModule = cms.untracked.bool(True),
    memoryPerEvent = cms.untracked.bool(True)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
