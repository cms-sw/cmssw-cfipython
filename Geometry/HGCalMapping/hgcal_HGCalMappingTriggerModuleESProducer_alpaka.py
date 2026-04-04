import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingTriggerModuleESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingTriggerModuleESProducer@alpaka',
    filename = cms.required.FileInPath,
    moduleindexer = cms.ESInputTag('', ''),
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
