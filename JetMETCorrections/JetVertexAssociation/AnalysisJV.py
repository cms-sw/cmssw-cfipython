import FWCore.ParameterSet.Config as cms

def AnalysisJV(**kwargs):
  mod = cms.EDAnalyzer('AnalysisJV',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
