import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerB = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerB',
  appendToDataLabel = cms.string('')
)
