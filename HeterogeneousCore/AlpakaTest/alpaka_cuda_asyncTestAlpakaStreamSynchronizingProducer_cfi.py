import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaStreamSynchronizingProducer = cms.EDProducer('alpaka_cuda_async::TestAlpakaStreamSynchronizingProducer',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
