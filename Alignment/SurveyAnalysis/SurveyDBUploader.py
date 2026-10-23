import FWCore.ParameterSet.Config as cms

def SurveyDBUploader(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyDBUploader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
