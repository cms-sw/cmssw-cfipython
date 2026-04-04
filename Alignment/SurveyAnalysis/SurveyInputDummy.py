import FWCore.ParameterSet.Config as cms

def SurveyInputDummy(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyInputDummy',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
