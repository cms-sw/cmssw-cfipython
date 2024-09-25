import FWCore.ParameterSet.Config as cms

def HcalDbAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDbAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
