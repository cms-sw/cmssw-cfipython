import FWCore.ParameterSet.Config as cms

def RctDigiToSourceCardText(*args, **kwargs):
  mod = cms.EDAnalyzer('RctDigiToSourceCardText',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
