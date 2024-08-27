import FWCore.ParameterSet.Config as cms

def PPSDiamondSampicTimingCalibrationPCLWorker(**kwargs):
  mod = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLWorker',
    totemTimingDigiTags = cms.VInputTag('totemTimingRawToDigi:TotemTiming'),
    totemTimingRecHitTags = cms.VInputTag('totemTimingRecHits'),
    folder = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
