import FWCore.ParameterSet.Config as cms

def HcalLutAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalLutAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
