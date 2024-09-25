import FWCore.ParameterSet.Config as cms

def HcalGainsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalGainsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
