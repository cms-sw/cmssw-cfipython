import FWCore.ParameterSet.Config as cms

def HcalDigiAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
