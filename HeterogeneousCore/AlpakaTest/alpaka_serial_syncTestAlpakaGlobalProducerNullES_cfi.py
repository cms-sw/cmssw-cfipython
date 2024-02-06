import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducerNullES = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerNullES',
  eventSetupSource = cms.ESInputTag('', ''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
