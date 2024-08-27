import FWCore.ParameterSet.Config as cms

def CocoaAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CocoaAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
