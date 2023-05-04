import FWCore.ParameterSet.Config as cms

roCmTestWrapperAdditionModule = cms.EDAnalyzer('ROCmTestWrapperAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
