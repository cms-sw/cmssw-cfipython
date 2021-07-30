import FWCore.ParameterSet.Config as cms

SimpleMemoryCheck = cms.Service('SimpleMemoryCheck',
  ignoreTotal = cms.untracked.int32(1),
  showMallocInfo = cms.untracked.bool(False),
  oncePerEventMode = cms.untracked.bool(False),
  jobReportOutputOnly = cms.untracked.bool(False),
  monitorPssAndPrivate = cms.untracked.bool(False),
  moduleMemorySummary = cms.untracked.bool(False),
  M_MMAP_MAX = cms.untracked.int32(-1),
  M_TRIM_THRESHOLD = cms.untracked.int32(-1),
  M_TOP_PAD = cms.untracked.int32(-1),
  M_MMAP_THRESHOLD = cms.untracked.int32(-1),
  dump = cms.untracked.bool(False)
)
