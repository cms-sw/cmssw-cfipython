import FWCore.ParameterSet.Config as cms

LockService = cms.Service('LockService',
  labels = cms.untracked.vstring(),
  lockSources = cms.untracked.bool(True)
)
