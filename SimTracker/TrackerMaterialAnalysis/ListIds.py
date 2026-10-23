import FWCore.ParameterSet.Config as cms

def ListIds(*args, **kwargs):
  mod = cms.EDAnalyzer('ListIds',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
