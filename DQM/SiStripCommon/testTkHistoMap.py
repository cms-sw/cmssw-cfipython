import FWCore.ParameterSet.Config as cms

def testTkHistoMap(*args, **kwargs):
  mod = cms.EDProducer('testTkHistoMap',
    readFromFile = cms.bool(False),
    inputFile = cms.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
