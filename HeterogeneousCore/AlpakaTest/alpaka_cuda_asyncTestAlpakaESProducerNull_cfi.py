import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerNull = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerNull',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
