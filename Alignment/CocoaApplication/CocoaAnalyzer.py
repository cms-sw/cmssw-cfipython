import FWCore.ParameterSet.Config as cms

def CocoaAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('CocoaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
