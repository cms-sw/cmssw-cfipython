import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationForHLTSoAESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('SiPixelGainCalibrationForHLTSoAESProducer@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
