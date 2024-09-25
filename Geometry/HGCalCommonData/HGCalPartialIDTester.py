import FWCore.ParameterSet.Config as cms

def HGCalPartialIDTester(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCalPartialIDTester',
    nameDetector = cms.string('HGCalEESensitive'),
    fileName = cms.string('partialD98.txt'),
    invert = cms.bool(False),
    debug = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
