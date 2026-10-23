import FWCore.ParameterSet.Config as cms

def CTPPSDiamondRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('CTPPSDiamondRecHitProducer',
    digiTag = cms.InputTag('ctppsDiamondRawToDigi', 'TimingDiamond'),
    timingCalibrationTag = cms.string(':PPSDiamondTimingCalibration'),
    timeSliceNs = cms.double(0.0244140625),
    applyCalibration = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
