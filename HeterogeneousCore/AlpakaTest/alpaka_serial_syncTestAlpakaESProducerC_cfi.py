import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerC = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerC',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)