import FWCore.ParameterSet.Config as cms

def DTSurveyConvert(*args, **kwargs):
  mod = cms.EDAnalyzer('DTSurveyConvert',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
