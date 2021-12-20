import FWCore.ParameterSet.Config as cms

SimpleMemoryCheck = cms.Service('SimpleMemoryCheck',
  ignoreTotal = cms.untracked.int32(1),
  showMallocInfo = cms.untracked.bool(False),
  oncePerEventMode = cms.untracked.bool(False),
  jobReportOutputOnly = cms.untracked.bool(False),
  monitorPssAndPrivate = cms.untracked.bool(False),
  moduleMemorySummary = cms.untracked.bool(False),
  dump = cms.untracked.bool(False)
)
