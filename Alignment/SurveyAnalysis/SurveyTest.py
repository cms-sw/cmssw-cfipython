import FWCore.ParameterSet.Config as cms

def SurveyTest(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
