import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncTestAlpakaESProducerD = cms.ESProducer('alpaka_rocm_async::TestAlpakaESProducerD',
  srcA = cms.ESInputTag('', ''),
  srcB = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
