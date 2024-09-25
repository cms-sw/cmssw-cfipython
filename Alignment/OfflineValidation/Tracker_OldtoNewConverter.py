import FWCore.ParameterSet.Config as cms

def Tracker_OldtoNewConverter(*args, **kwargs):
  mod = cms.EDAnalyzer('Tracker_OldtoNewConverter',
    conversionType = cms.untracked.string(''),
    inputFile = cms.untracked.string(''),
    outputFile = cms.untracked.string(''),
    textFile = cms.untracked.string(''),
    treeName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
