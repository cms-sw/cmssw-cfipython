import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationPCLWorker(**kwargs):
  mod = cms.EDProducer('PPSTimingCalibrationPCLWorker',
    diamondRecHitTags = cms.VInputTag('ctppsDiamondRecHits'),
    dqmDir = cms.string('AlCaReco/PPSTimingCalibrationPCL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
