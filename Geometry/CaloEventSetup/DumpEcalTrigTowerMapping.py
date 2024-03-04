import FWCore.ParameterSet.Config as cms

def DumpEcalTrigTowerMapping(**kwargs):
  mod = cms.EDAnalyzer('DumpEcalTrigTowerMapping',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
