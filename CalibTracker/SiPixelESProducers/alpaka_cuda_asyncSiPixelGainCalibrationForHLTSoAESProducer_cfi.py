import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncSiPixelGainCalibrationForHLTSoAESProducer = cms.ESProducer('alpaka_cuda_async::SiPixelGainCalibrationForHLTSoAESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
