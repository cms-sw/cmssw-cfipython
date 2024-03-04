import FWCore.ParameterSet.Config as cms

def SiStripBadStripFromASCIIFile(**kwargs):
  mod = cms.EDAnalyzer('SiStripBadStripFromASCIIFile',
    SinceAppendMode = cms.required.bool,
    IOVMode = cms.required.string,
    Record = cms.required.string,
    doStoreOnDB = cms.required.bool,
    TimeFromEndRun = cms.untracked.bool(False),
    TimeFromStartOfRunRange = cms.untracked.bool(False),
    file = cms.FileInPath('CondTools/SiStrip/data/DefectsFromConstructionDB.dat'),
    printDebug = cms.bool(False),
    isFlagAvailable = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
