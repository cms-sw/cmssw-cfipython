import FWCore.ParameterSet.Config as cms

CondorStatusService = cms.Service('CondorStatusService',
  updateIntervalSeconds = cms.untracked.uint32(180),
  debug = cms.untracked.bool(False),
  EMAInterval = cms.untracked.double(900)
)
