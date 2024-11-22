import FWCore.ParameterSet.Config as cms

def HcalTB06Analysis(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTB06Analysis',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
