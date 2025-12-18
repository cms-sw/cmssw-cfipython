import FWCore.ParameterSet.Config as cms

def trackerDTC_Analyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('trackerDTC::Analyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
