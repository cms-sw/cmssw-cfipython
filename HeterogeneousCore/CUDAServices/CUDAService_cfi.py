import FWCore.ParameterSet.Config as cms

CUDAService = cms.Service('CUDAService',
  enabled = cms.untracked.bool(True),
  limits = cms.untracked.PSet(
    cudaLimitPrintfFifoSize = cms.untracked.int32(-1),
    cudaLimitStackSize = cms.untracked.int32(-1),
    cudaLimitMallocHeapSize = cms.untracked.int32(-1),
    cudaLimitDevRuntimeSyncDepth = cms.untracked.int32(-1),
    cudaLimitDevRuntimePendingLaunchCount = cms.untracked.int32(-1)
  ),
  allocator = cms.untracked.PSet(
    devicePreallocate = cms.untracked.vuint32(),
    hostPreallocate = cms.untracked.vuint32()
  )
)
