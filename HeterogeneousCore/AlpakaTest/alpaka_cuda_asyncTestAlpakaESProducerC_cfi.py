import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerC = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerC',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
