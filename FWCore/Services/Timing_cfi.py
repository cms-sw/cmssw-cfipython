import FWCore.ParameterSet.Config as cms

Timing = cms.Service('Timing',
  summaryOnly = cms.untracked.bool(False),
  useJobReport = cms.untracked.bool(True),
  excessiveTimeThreshold = cms.untracked.double(0)
)
