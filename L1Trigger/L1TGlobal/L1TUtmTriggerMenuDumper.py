import FWCore.ParameterSet.Config as cms

def L1TUtmTriggerMenuDumper(*args, **kwargs):
  mod = cms.EDAnalyzer('L1TUtmTriggerMenuDumper',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
