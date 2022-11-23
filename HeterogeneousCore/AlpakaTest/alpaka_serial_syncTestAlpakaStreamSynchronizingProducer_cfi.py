import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaStreamSynchronizingProducer = cms.EDProducer('alpaka_serial_sync::TestAlpakaStreamSynchronizingProducer',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
