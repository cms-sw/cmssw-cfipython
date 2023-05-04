import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncTestAlpakaESProducerB = cms.ESProducer('alpaka_cuda_async::TestAlpakaESProducerB',
  explicitLabel = cms.string(''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
