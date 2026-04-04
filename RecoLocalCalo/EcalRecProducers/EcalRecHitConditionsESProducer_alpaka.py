import FWCore.ParameterSet.Config as cms

def EcalRecHitConditionsESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('EcalRecHitConditionsESProducer@alpaka',
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
