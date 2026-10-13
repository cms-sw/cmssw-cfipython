import FWCore.ParameterSet.Config as cms

def HGCalAreaTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalAreaTester',
    nameDetector = cms.string('HGCalHEScintillatorSensitive'),
    fileName = cms.string('detID.txt'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
