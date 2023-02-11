import FWCore.ParameterSet.Config as cms

ROCmService = cms.Service('ROCmService',
  enabled = cms.untracked.bool(True),
  verbose = cms.untracked.bool(False),
  limits = cms.untracked.PSet(
    hipLimitStackSize = cms.untracked.int32(-1),
    hipLimitMallocHeapSize = cms.untracked.int32(-1),
    hipLimitDevRuntimeSyncDepth = cms.untracked.int32(-1),
    hipLimitDevRuntimePendingLaunchCount = cms.untracked.int32(-1)
  )
)
