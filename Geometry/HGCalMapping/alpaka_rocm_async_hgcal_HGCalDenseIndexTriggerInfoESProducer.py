import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_hgcal_HGCalDenseIndexTriggerInfoESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::hgcal::HGCalDenseIndexTriggerInfoESProducer',
    moduleindexer = cms.ESInputTag('', ''),
    cellindexer = cms.ESInputTag('', ''),
    moduleinfo = cms.ESInputTag('', ''),
    cellinfo = cms.ESInputTag('', ''),
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
