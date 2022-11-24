import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaStreamProducer = cms.EDProducer('alpaka_cuda_async::TestAlpakaStreamProducer',
  source = cms.required.InputTag,
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
