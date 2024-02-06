import FWCore.ParameterSet.Config as cms

alpaka_serial_syncSiPixelCablingSoAESProducer = cms.ESProducer('alpaka_serial_sync::SiPixelCablingSoAESProducer',
  CablingMapLabel = cms.string(''),
  UseQualityInfo = cms.bool(False),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
