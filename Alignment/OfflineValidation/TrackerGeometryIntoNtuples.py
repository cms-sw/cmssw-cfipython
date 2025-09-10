import FWCore.ParameterSet.Config as cms

def TrackerGeometryIntoNtuples(*args, **kwargs):
  mod = cms.EDAnalyzer('TrackerGeometryIntoNtuples',
    outputFile = cms.untracked.string(''),
    outputTreename = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
