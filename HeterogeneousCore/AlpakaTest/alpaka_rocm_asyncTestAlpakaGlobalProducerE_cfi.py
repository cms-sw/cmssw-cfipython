import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaGlobalProducerE = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerE',
  eventSetupSource = cms.ESInputTag('', ''),
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
