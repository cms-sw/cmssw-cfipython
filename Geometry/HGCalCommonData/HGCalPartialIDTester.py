import FWCore.ParameterSet.Config as cms

def HGCalPartialIDTester(**kwargs):
  mod = cms.EDAnalyzer('HGCalPartialIDTester',
    nameDetector = cms.string('HGCalEESensitive'),
    fileName = cms.string('partialD98.txt'),
    invert = cms.bool(False),
    debug = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
