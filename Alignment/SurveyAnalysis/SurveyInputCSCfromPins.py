import FWCore.ParameterSet.Config as cms

def SurveyInputCSCfromPins(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyInputCSCfromPins',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
