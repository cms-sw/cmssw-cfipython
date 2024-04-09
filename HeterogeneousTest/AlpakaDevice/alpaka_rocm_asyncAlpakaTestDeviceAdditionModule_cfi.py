import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncAlpakaTestDeviceAdditionModule = cms.EDAnalyzer('alpaka_rocm_async::AlpakaTestDeviceAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
