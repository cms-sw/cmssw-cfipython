import FWCore.ParameterSet.Config as cms

def HcalTBObjectDump(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalTBObjectDump',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
