import FWCore.ParameterSet.Config as cms

def HGCalScintIDTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalScintIDTester',
    nameSense = cms.string('HGCalHEScintillatorSensitive'),
    fileName = cms.string('errorScintD88.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
