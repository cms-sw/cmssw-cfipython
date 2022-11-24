import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerD = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerD',
  appendToDataLabel = cms.string('')
)
