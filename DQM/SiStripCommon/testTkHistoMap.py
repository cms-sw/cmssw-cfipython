import FWCore.ParameterSet.Config as cms

def testTkHistoMap(**kwargs):
  mod = cms.EDProducer('testTkHistoMap',
    readFromFile = cms.bool(False),
    inputFile = cms.FileInPath('CalibTracker/SiStripCommon/data/SiStripDetInfo.dat'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
