import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerE = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerE',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
