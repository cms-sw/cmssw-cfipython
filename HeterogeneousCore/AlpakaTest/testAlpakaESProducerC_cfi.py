import FWCore.ParameterSet.Config as cms

testAlpakaESProducerC = cms.ESProducer('TestAlpakaESProducerC@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
