import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingModuleESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingModuleESProducer@alpaka',
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
