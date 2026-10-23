import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_sistrip_SiStripClusterizerConditionsESProducerAlpaka(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::sistrip::SiStripClusterizerConditionsESProducerAlpaka',
    QualityLabel = cms.ESInputTag('', ''),
    Label = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
