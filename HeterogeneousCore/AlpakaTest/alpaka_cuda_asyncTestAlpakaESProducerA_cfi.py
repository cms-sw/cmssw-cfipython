import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerA = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerA',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
