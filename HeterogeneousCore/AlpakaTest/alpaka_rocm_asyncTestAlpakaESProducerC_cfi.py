import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerC = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerC',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
