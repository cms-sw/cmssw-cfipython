import FWCore.ParameterSet.Config as cms

testAlpakaESProducerB = cms.ESProducer('TestAlpakaESProducerB@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
