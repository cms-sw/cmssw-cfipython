import FWCore.ParameterSet.Config as cms

roCmTestDeviceAdditionModule = cms.EDAnalyzer('ROCmTestDeviceAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
