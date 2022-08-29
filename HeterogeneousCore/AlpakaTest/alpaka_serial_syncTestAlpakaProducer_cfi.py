import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaProducer = cms.EDProducer('alpaka_serial_sync::TestAlpakaProducer',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
