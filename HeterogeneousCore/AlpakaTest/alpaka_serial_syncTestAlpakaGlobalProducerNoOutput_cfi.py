import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaGlobalProducerNoOutput = cms.EDProducer('alpaka_serial_sync::TestAlpakaGlobalProducerNoOutput',
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
