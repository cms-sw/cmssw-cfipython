import FWCore.ParameterSet.Config as cms

alpaka_serial_syncHcalMahiConditionsESProducer = cms.ESProducer('alpaka_serial_sync::HcalMahiConditionsESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
