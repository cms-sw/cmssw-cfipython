import FWCore.ParameterSet.Config as cms

alpaka_serial_syncEcalElectronicsMappingHostESProducer = cms.ESProducer('alpaka_serial_sync::EcalElectronicsMappingHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
