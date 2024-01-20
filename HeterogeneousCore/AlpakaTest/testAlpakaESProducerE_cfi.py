import FWCore.ParameterSet.Config as cms

testAlpakaESProducerE = cms.ESProducer('TestAlpakaESProducerE@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
