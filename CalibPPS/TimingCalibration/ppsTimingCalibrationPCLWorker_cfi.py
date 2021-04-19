import FWCore.ParameterSet.Config as cms

ppsTimingCalibrationPCLWorker = cms.EDProducer('PPSTimingCalibrationPCLWorker',
  diamondRecHitTag = cms.InputTag('ctppsDiamondUncalibRecHits'),
  dqmDir = cms.string('AlCaReco/PPSTimingCalibrationPCL'),
  mightGet = cms.optional.untracked.vstring
)
