import FWCore.ParameterSet.Config as cms

cudaTestKernelAdditionModule = cms.EDAnalyzer('CUDATestKernelAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
