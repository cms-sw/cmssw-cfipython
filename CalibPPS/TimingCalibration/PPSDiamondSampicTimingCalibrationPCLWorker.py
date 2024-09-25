import FWCore.ParameterSet.Config as cms

def PPSDiamondSampicTimingCalibrationPCLWorker(*args, **kwargs):
  mod = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLWorker',
    totemTimingDigiTags = cms.VInputTag('totemTimingRawToDigi:TotemTiming'),
    totemTimingRecHitTags = cms.VInputTag('totemTimingRecHits'),
    folder = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
