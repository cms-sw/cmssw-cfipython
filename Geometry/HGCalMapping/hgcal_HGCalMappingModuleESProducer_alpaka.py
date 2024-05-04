import FWCore.ParameterSet.Config as cms

def hgcal_HGCalMappingModuleESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('hgcal::HGCalMappingModuleESProducer@alpaka',
    filename = cms.required.FileInPath,
    moduleindexer = cms.ESInputTag('', ''),
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
