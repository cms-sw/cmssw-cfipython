import FWCore.ParameterSet.Config as cms

def DumpEcalTrigTowerMapping(*args, **kwargs):
  mod = cms.EDAnalyzer('DumpEcalTrigTowerMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
