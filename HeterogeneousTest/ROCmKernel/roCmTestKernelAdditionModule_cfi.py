import FWCore.ParameterSet.Config as cms

roCmTestKernelAdditionModule = cms.EDAnalyzer('ROCmTestKernelAdditionModule',
  size = cms.uint32(1048576),
  mightGet = cms.optional.untracked.vstring
)
