import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerA = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerA',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
