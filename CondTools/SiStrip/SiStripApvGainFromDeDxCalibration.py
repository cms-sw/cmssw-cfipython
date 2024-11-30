import FWCore.ParameterSet.Config as cms

def SiStripApvGainFromDeDxCalibration(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainFromDeDxCalibration',
    file = cms.untracked.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
    printDebug = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
