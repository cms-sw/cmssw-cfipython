import FWCore.ParameterSet.Config as cms

def SurveyDataConverter(**kwargs):
  mod = cms.EDAnalyzer('SurveyDataConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
