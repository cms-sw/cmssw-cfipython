import FWCore.ParameterSet.Config as cms

def LHEWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('LHEWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
