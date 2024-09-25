import FWCore.ParameterSet.Config as cms

def HcalCableMapper(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalCableMapper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
