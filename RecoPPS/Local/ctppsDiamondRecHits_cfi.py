import FWCore.ParameterSet.Config as cms

ctppsDiamondRecHits = cms.EDProducer('CTPPSDiamondRecHitProducer',
  digiTag = cms.InputTag('ctppsDiamondRawToDigi', 'TimingDiamond'),
  timingCalibrationTag = cms.string(':PPSDiamondTimingCalibration'),
  timeSliceNs = cms.double(0.0244140625),
  applyCalibration = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
