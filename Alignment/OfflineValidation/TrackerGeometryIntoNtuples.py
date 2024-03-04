import FWCore.ParameterSet.Config as cms

def TrackerGeometryIntoNtuples(**kwargs):
  mod = cms.EDAnalyzer('TrackerGeometryIntoNtuples',
    outputFile = cms.untracked.string(''),
    outputTreename = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
