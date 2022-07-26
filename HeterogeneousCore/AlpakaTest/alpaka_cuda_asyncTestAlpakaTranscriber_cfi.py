import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaTranscriber = cms.EDProducer('alpaka_cuda_async::TestAlpakaTranscriber',
  source = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
