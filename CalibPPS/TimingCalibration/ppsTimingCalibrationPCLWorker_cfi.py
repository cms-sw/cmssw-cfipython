import FWCore.ParameterSet.Config as cms

ppsTimingCalibrationPCLWorker = cms.EDProducer('PPSTimingCalibrationPCLWorker',
  diamondRecHitTags = cms.VInputTag('ctppsDiamondRecHits'),
  dqmDir = cms.string('AlCaReco/PPSTimingCalibrationPCL'),
  mightGet = cms.optional.untracked.vstring
)
