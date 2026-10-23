import FWCore.ParameterSet.Config as cms

def HcalQIEDataPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalQIEDataPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
