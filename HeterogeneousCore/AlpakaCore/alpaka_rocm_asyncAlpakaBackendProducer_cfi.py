import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncAlpakaBackendProducer = cms.EDProducer('alpaka_rocm_async::AlpakaBackendProducer',
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
