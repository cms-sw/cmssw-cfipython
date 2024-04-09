import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncAlpakaTestOpaqueAdditionModule = cms.EDAnalyzer('alpaka_cuda_async::AlpakaTestOpaqueAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
