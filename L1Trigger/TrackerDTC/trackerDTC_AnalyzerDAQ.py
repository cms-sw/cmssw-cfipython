import FWCore.ParameterSet.Config as cms

def trackerDTC_AnalyzerDAQ(**kwargs):
  mod = cms.EDAnalyzer('trackerDTC::AnalyzerDAQ',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
