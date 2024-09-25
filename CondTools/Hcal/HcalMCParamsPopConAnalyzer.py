import FWCore.ParameterSet.Config as cms

def HcalMCParamsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalMCParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
