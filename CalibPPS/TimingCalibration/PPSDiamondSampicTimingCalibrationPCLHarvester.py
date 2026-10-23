import FWCore.ParameterSet.Config as cms

def PPSDiamondSampicTimingCalibrationPCLHarvester(*args, **kwargs):
  mod = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLHarvester',
    timingCalibrationTag = cms.string('GlobalTag:PPSDiamondSampicCalibration'),
    dqmDir = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
    minEntries = cms.uint32(1),
    jsonCalibFile = cms.string(''),
    jsonOutputPath = cms.string('offset_cal.json'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
