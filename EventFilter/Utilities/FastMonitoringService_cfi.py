import FWCore.ParameterSet.Config as cms

FastMonitoringService = cms.Service('FastMonitoringService',
  tbbMonitoringMode = cms.untracked.bool(True),
  tbbConcurrencyTracker = cms.untracked.bool(True),
  sleepTime = cms.untracked.int32(1),
  fastMonIntervals = cms.untracked.uint32(2),
  filePerFwkStream = cms.untracked.bool(True),
  verbose = cms.untracked.bool(False)
)
