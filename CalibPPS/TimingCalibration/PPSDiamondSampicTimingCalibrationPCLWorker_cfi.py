import FWCore.ParameterSet.Config as cms

PPSDiamondSampicTimingCalibrationPCLWorker = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLWorker',
  totemTimingDigiTags = cms.VInputTag('totemTimingRawToDigi:TotemTiming'),
  totemTimingRecHitTags = cms.VInputTag('totemTimingRecHits'),
  folder = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
  mightGet = cms.optional.untracked.vstring
)
