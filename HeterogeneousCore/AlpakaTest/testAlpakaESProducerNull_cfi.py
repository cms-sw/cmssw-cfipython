import FWCore.ParameterSet.Config as cms

testAlpakaESProducerNull = cms.ESProducer('TestAlpakaESProducerNull@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
