import FWCore.ParameterSet.Config as cms

def hgcalrechit_HGCalConfigurationESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcalrechit::HGCalConfigurationESProducer@alpaka',
    indexSource = cms.ESInputTag('', ''),
    configSource = cms.ESInputTag('', ''),
    gain = cms.int32(2),
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
