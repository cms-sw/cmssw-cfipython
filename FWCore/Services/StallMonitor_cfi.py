import FWCore.ParameterSet.Config as cms

StallMonitor = cms.Service('StallMonitor',
  fileName = cms.untracked.string(''),
  stallThreshold = cms.untracked.double(0.1)
)
