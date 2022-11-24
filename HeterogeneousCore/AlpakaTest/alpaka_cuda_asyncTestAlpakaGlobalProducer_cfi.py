import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaGlobalProducer = cms.EDProducer('alpaka_cuda_async::TestAlpakaGlobalProducer',
  size = cms.required.int32,
  mightGet = cms.optional.untracked.vstring
)
