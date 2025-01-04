import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_EcalRecHitConditionsESProducer(*args, **kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::EcalRecHitConditionsESProducer',
    timeCalibTag = cms.ESInputTag('', ''),
    timeOffsetTag = cms.ESInputTag('', ''),
    isPhase2 = cms.bool(False),
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
