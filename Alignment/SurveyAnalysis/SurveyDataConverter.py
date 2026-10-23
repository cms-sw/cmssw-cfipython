import FWCore.ParameterSet.Config as cms

def SurveyDataConverter(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyDataConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
