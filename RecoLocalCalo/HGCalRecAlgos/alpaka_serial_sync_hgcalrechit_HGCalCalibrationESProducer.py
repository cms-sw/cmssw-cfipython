import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_hgcalrechit_HGCalCalibrationESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::hgcalrechit::HGCalCalibrationESProducer',
    filename = cms.required.FileInPath,
    filenameEnergyLoss = cms.required.FileInPath,
    indexSource = cms.ESInputTag('', ''),
    mapSource = cms.ESInputTag('', ''),
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
