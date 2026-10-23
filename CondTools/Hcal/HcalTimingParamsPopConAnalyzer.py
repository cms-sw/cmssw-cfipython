import FWCore.ParameterSet.Config as cms

def HcalTimingParamsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTimingParamsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
