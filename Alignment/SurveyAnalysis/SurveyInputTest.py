import FWCore.ParameterSet.Config as cms

def SurveyInputTest(**kwargs):
  mod = cms.EDAnalyzer('SurveyInputTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
