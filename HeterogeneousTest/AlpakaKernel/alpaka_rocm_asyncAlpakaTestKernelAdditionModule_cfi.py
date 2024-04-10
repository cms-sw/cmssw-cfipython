import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncAlpakaTestKernelAdditionModule = cms.EDAnalyzer('alpaka_rocm_async::AlpakaTestKernelAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
