import FWCore.ParameterSet.Config as cms

testAlpakaESProducerD = cms.ESProducer('TestAlpakaESProducerD@alpaka',
  srcA = cms.ESInputTag('', ''),
  srcB = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
