import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerB = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerB',
  appendToDataLabel = cms.string('')
)
