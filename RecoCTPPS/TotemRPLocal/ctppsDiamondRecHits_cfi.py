import FWCore.ParameterSet.Config as cms

ctppsDiamondRecHits = cms.EDProducer('CTPPSDiamondRecHitProducer',
  digiTag = cms.InputTag('ctppsDiamondRawToDigi', 'TimingDiamond'),
  timingCalibrationTag = cms.string('GlobalTag:PPSDiamondTimingCalibration'),
  timeSliceNs = cms.double(0.0244140625),
  timeShift = cms.int32(0),
  mightGet = cms.optional.untracked.vstring
)
