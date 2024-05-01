import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaGlobalProducerNoOutput = cms.EDProducer('alpaka_rocm_async::TestAlpakaGlobalProducerNoOutput',
  source = cms.InputTag(''),
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
