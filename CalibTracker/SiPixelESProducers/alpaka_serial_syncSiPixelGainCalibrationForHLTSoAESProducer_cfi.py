import FWCore.ParameterSet.Config as cms

alpaka_serial_syncSiPixelGainCalibrationForHLTSoAESProducer = cms.ESProducer('alpaka_serial_sync::SiPixelGainCalibrationForHLTSoAESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
