import FWCore.ParameterSet.Config as cms

def writeBlob(*args, **kwargs):
  mod = cms.EDAnalyzer('writeBlob',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
