import FWCore.ParameterSet.Config as cms

def HcalDcsMapPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDcsMapPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
