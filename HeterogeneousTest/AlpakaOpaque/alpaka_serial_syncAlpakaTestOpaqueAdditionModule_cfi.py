import FWCore.ParameterSet.Config as cms

alpaka_serial_syncAlpakaTestOpaqueAdditionModule = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestOpaqueAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
