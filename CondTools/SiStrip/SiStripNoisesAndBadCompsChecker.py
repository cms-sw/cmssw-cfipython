import FWCore.ParameterSet.Config as cms

def SiStripNoisesAndBadCompsChecker(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripNoisesAndBadCompsChecker',
    writePayload = cms.untracked.bool(True),
    file = cms.untracked.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
    printDebug = cms.untracked.uint32(4294967295),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
