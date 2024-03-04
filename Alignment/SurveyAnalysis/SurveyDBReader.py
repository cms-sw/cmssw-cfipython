import FWCore.ParameterSet.Config as cms

def SurveyDBReader(**kwargs):
  mod = cms.EDAnalyzer('SurveyDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
