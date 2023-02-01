import FWCore.ParameterSet.Config as cms

testAlpakaESProducerD = cms.ESProducer('TestAlpakaESProducerD@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
