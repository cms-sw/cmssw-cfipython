import FWCore.ParameterSet.Config as cms

def HcalSevLvlAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalSevLvlAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
