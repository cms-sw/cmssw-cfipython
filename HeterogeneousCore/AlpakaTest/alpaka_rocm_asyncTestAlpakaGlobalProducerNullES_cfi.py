import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaGlobalProducerNullES = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerNullES',
  eventSetupSource = cms.ESInputTag('', ''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
