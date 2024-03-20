import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerB = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerB',
  explicitLabel = cms.string(''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
