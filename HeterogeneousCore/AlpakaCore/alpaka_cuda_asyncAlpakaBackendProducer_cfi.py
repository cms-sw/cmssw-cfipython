import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncAlpakaBackendProducer = cms.EDProducer('alpaka_cuda_async::AlpakaBackendProducer',
  mightGet = cms.optional.untracked.vstring,
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
