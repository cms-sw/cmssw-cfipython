import FWCore.ParameterSet.Config as cms

alpaka_serial_syncEcalMultifitConditionsHostESProducer = cms.ESProducer('alpaka_serial_sync::EcalMultifitConditionsHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)