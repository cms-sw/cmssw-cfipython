import FWCore.ParameterSet.Config as cms

alpaka_serial_syncAlpakaTestWrapperAdditionModule = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestWrapperAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
