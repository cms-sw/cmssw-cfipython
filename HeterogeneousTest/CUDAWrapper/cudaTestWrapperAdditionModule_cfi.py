import FWCore.ParameterSet.Config as cms

cudaTestWrapperAdditionModule = cms.EDAnalyzer('CUDATestWrapperAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
