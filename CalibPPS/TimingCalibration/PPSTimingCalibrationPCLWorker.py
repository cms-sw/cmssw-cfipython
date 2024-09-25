import FWCore.ParameterSet.Config as cms

def PPSTimingCalibrationPCLWorker(*args, **kwargs):
  mod = cms.EDProducer('PPSTimingCalibrationPCLWorker',
    diamondRecHitTags = cms.VInputTag('ctppsDiamondRecHits'),
    dqmDir = cms.string('AlCaReco/PPSTimingCalibrationPCL'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
