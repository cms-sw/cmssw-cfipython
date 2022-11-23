import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaStreamProducer = cms.EDProducer('alpaka_serial_sync::TestAlpakaStreamProducer',
  source = cms.required.InputTag,
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
