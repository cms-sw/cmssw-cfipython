import FWCore.ParameterSet.Config as cms

def HcalValidationCorrsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalValidationCorrsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
