import FWCore.ParameterSet.Config as cms

FastMonitoringService = cms.Service('FastMonitoringService',
  sleepTime = cms.untracked.int32(1),
  fastMonIntervals = cms.untracked.uint32(2),
  filePerFwkStream = cms.untracked.bool(False)
)
