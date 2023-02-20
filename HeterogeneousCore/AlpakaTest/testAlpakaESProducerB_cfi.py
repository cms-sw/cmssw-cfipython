import FWCore.ParameterSet.Config as cms

testAlpakaESProducerB = cms.ESProducer('TestAlpakaESProducerB@alpaka',
  explicitLabel = cms.string(''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
