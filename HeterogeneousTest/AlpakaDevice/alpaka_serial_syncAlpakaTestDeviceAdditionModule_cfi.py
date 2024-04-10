import FWCore.ParameterSet.Config as cms

alpaka_serial_syncAlpakaTestDeviceAdditionModule = cms.EDAnalyzer('alpaka_serial_sync::AlpakaTestDeviceAdditionModule',
  size = cms.uint32(1048576),
  alpaka = cms.untracked.PSet(),
  mightGet = cms.optional.untracked.vstring
)
