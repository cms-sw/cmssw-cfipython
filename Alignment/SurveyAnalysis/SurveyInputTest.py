import FWCore.ParameterSet.Config as cms

def SurveyInputTest(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyInputTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
