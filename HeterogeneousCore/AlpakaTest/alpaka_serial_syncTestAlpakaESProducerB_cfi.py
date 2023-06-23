import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerB = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerB',
  explicitLabel = cms.string(''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)