import FWCore.ParameterSet.Config as cms

def SurveyDBReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyDBReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
