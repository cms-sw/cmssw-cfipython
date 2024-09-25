import FWCore.ParameterSet.Config as cms

def HcalTBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTBWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
