import FWCore.ParameterSet.Config as cms

def SimpleMemoryCheck(*args, **kwargs):
  mod = cms.Service('SimpleMemoryCheck',
    ignoreTotal = cms.untracked.int32(1),
    sampleEveryNSeconds = cms.untracked.uint32(0),
    showMallocInfo = cms.untracked.bool(False),
    oncePerEventMode = cms.untracked.bool(False),
    jobReportOutputOnly = cms.untracked.bool(False),
    monitorPssAndPrivate = cms.untracked.bool(False),
    moduleMemorySummary = cms.untracked.bool(False)
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
