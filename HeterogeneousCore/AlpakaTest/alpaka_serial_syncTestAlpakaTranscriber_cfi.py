import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaTranscriber = cms.EDProducer('alpaka_serial_sync::TestAlpakaTranscriber',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
