import FWCore.ParameterSet.Config as cms

ConcurrentModuleTimer = cms.Service('ConcurrentModuleTimer',
  modulesToExclude = cms.untracked.vstring(),
  excludeSource = cms.untracked.bool(False),
  padding = cms.untracked.uint32(0),
  trackGlobalBeginRun = cms.untracked.bool(False)
)
