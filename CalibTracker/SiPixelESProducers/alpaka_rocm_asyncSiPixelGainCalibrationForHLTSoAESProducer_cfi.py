import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncSiPixelGainCalibrationForHLTSoAESProducer = cms.ESProducer('alpaka_rocm_async::SiPixelGainCalibrationForHLTSoAESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
