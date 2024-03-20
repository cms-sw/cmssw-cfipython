import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerE = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerE',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
