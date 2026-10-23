import FWCore.ParameterSet.Config as cms

def SurveyInputTrackerFromDB(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyInputTrackerFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
