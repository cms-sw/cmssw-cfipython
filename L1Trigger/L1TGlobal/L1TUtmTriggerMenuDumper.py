import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuDumper(**kwargs):
  mod = cms.EDAnalyzer('L1TUtmTriggerMenuDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
