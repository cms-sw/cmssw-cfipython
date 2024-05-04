import FWCore.ParameterSet.Config as cms

alpaka_serial_synchgcalHGCalMappingModuleESProducer = cms.ESProducer('alpaka_serial_sync::hgcal::HGCalMappingModuleESProducer',
  filename = cms.required.FileInPath,
  moduleindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
