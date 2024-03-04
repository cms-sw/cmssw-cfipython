import FWCore.ParameterSet.Config as cms

def trackerDTC_Analyzer(**kwargs):
  mod = cms.EDAnalyzer('trackerDTC::Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
