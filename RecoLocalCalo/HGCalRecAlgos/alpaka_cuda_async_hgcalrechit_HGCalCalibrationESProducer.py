import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_hgcalrechit_HGCalCalibrationESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::hgcalrechit::HGCalCalibrationESProducer',
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
