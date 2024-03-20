import FWCore.ParameterSet.Config as cms

testAlpakaESProducerA = cms.ESProducer('TestAlpakaESProducerA@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
