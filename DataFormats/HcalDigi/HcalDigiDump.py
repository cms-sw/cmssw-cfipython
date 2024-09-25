import FWCore.ParameterSet.Config as cms

def HcalDigiDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDigiDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
