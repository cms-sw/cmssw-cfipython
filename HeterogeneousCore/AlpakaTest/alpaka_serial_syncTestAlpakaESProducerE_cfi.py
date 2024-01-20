import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerE = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerE',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
