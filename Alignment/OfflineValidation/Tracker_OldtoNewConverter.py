import FWCore.ParameterSet.Config as cms

def Tracker_OldtoNewConverter(**kwargs):
  mod = cms.EDAnalyzer('Tracker_OldtoNewConverter',
    conversionType = cms.untracked.string(''),
    inputFile = cms.untracked.string(''),
    outputFile = cms.untracked.string(''),
    textFile = cms.untracked.string(''),
    treeName = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
