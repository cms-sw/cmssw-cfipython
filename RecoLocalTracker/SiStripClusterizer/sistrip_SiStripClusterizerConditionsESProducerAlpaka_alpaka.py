import FWCore.ParameterSet.Config as cms

def sistrip_SiStripClusterizerConditionsESProducerAlpaka_alpaka(*args, **kwargs):
  mod = cms.ESProducer('sistrip::SiStripClusterizerConditionsESProducerAlpaka@alpaka',
    QualityLabel = cms.required.ESInputTag,
    Label = cms.required.ESInputTag,
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
