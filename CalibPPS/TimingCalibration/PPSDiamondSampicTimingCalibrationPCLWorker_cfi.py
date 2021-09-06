import FWCore.ParameterSet.Config as cms

PPSDiamondSampicTimingCalibrationPCLWorker = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLWorker',
  totemTimingDigiTag = cms.InputTag('totemTimingRawToDigi', 'TotemTiming'),
  totemTimingRecHitTag = cms.InputTag('totemTimingRecHits'),
  folder = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
  mightGet = cms.optional.untracked.vstring
)
