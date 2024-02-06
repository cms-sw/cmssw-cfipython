import FWCore.ParameterSet.Config as cms

roCmTestOpaqueAdditionModule = cms.EDAnalyzer('ROCmTestOpaqueAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
