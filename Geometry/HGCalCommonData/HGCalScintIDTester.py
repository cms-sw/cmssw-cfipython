import FWCore.ParameterSet.Config as cms

def HGCalScintIDTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalScintIDTester',
    nameSense = cms.string('HGCalHEScintillatorSensitive'),
    fileName = cms.string('errorScintD88.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
