import FWCore.ParameterSet.Config as cms

cudaTestOpaqueAdditionModule = cms.EDAnalyzer('CUDATestOpaqueAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
