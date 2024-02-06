import FWCore.ParameterSet.Config as cms

alpaka_serial_syncTestAlpakaESProducerNull = cms.ESProducer('alpaka_serial_sync::TestAlpakaESProducerNull',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
