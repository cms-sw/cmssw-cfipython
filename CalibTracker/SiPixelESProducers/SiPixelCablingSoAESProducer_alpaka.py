import FWCore.ParameterSet.Config as cms

def SiPixelCablingSoAESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('SiPixelCablingSoAESProducer@alpaka',
    CablingMapLabel = cms.string(''),
    UseQualityInfo = cms.bool(False),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
