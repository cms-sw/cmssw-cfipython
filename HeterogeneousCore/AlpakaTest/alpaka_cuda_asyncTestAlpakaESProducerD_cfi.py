import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerD = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerD',
  appendToDataLabel = cms.string('')
)
