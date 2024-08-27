import FWCore.ParameterSet.Config as cms

def CUDAMonitoringService(**kwargs):
  mod = cms.Service('CUDAMonitoringService',
    memoryConstruction = cms.untracked.bool(False),
    memoryBeginStream = cms.untracked.bool(True),
    memoryPerModule = cms.untracked.bool(True),
    memoryPerEvent = cms.untracked.bool(True)
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
