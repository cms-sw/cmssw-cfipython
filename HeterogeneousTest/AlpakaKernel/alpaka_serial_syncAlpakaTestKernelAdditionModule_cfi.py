import FWCore.ParameterSet.Config as cms

alpaka_serial_syncAlpakaTestKernelAdditionModule = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestKernelAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
