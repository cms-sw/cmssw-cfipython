import FWCore.ParameterSet.Config as cms

PPSDiamondSampicTimingCalibrationPCLHarvester = cms.EDProducer('PPSDiamondSampicTimingCalibrationPCLHarvester',
  timingCalibrationTag = cms.string('GlobalTag:PPSDiamondSampicCalibration'),
  dqmDir = cms.string('AlCaReco/PPSDiamondSampicTimingCalibrationPCL'),
  minEntries = cms.uint32(1),
  jsonCalibFile = cms.string(''),
  jsonOutputPath = cms.string('offset_cal.json'),
  mightGet = cms.optional.untracked.vstring
)
