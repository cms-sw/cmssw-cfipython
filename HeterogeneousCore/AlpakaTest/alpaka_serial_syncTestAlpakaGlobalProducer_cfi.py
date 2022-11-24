import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducer = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducer',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
