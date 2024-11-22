import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_hgcal_HGCalMappingModuleESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_serial_sync::hgcal::HGCalMappingModuleESProducer',
    filename = cms.required.FileInPath,
    moduleindexer = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
