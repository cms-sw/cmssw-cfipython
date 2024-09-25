import FWCore.ParameterSet.Config as cms

def HcalTPParametersPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTPParametersPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
