import FWCore.ParameterSet.Config as cms

def SiPixelGainCalibrationRejectNoisyAndDead(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelGainCalibrationRejectNoisyAndDead',
    debug = cms.untracked.bool(False),
    insertNoisyPixelsInDB = cms.untracked.int32(1),
    record = cms.untracked.string('SiPixelGainCalibrationOfflineRcd'),
    noisyPixelList = cms.untracked.string('noisypixel.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
