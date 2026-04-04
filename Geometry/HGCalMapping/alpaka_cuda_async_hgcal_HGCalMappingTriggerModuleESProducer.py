import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_hgcal_HGCalMappingTriggerModuleESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::hgcal::HGCalMappingTriggerModuleESProducer',
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
