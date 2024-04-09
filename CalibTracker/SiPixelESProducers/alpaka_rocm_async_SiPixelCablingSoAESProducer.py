import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_SiPixelCablingSoAESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::SiPixelCablingSoAESProducer',
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