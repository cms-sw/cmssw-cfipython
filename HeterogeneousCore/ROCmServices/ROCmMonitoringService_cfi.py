import FWCore.ParameterSet.Config as cms

ROCmMonitoringService = cms.Service('ROCmMonitoringService',
  memoryConstruction = cms.untracked.bool(False),
  memoryBeginStream = cms.untracked.bool(True),
  memoryPerModule = cms.untracked.bool(True),
  memoryPerEvent = cms.untracked.bool(True)
)
