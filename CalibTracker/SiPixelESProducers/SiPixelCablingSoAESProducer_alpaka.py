import FWCore.ParameterSet.Config as cms

def SiPixelCablingSoAESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('SiPixelCablingSoAESProducer@alpaka',
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
