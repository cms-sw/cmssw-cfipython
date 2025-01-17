import FWCore.ParameterSet.Config as cms

def hgcalrechit_HGCalCalibrationESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcalrechit::HGCalCalibrationESProducer@alpaka',
    filename = cms.required.FileInPath,
    indexSource = cms.ESInputTag('', ''),
    configSource = cms.ESInputTag('', ''),
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
