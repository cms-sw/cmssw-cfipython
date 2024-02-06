import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerA = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerA',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
