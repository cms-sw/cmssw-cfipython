import FWCore.ParameterSet.Config as cms

def SurveyMisalignmentInput(*args, **kwargs):
  mod = cms.EDAnalyzer('SurveyMisalignmentInput',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
