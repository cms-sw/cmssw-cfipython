import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerNull = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerNull',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
