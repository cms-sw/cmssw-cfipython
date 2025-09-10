import FWCore.ParameterSet.Config as cms

def L1MenuViewer(*args, **kwargs):
  mod = cms.EDAnalyzer('L1MenuViewer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
