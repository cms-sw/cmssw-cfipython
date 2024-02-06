import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerD = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerD',
  srcA = cms.ESInputTag('', ''),
  srcB = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
