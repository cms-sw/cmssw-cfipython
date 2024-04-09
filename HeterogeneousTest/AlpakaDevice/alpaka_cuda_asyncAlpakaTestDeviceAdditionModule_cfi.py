import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncAlpakaTestDeviceAdditionModule = cms.EDAnalyzer('alpaka_cuda_async::AlpakaTestDeviceAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
