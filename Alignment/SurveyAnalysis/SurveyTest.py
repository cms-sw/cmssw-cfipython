import FWCore.ParameterSet.Config as cms

def SurveyTest(**kwargs):
  mod = cms.EDAnalyzer('SurveyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
