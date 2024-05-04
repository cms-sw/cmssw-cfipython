import FWCore.ParameterSet.Config as cms

alpaka_serial_synchgcalHGCalMappingCellESProducer = cms.ESProducer('alpaka_serial_sync::hgcal::HGCalMappingCellESProducer',
  filelist = cms.vstring(),
  cellindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
