import FWCore.ParameterSet.Config as cms

cudaTestDeviceAdditionModule = cms.EDAnalyzer('CUDATestDeviceAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
