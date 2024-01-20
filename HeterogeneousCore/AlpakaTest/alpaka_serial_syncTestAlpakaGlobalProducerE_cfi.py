import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducerE = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerE',
  eventSetupSource = cms.ESInputTag('', ''),
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
