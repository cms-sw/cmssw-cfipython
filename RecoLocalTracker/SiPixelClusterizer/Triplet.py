import FWCore.ParameterSet.Config as cms

def Triplet(*args, **kwargs):
  mod = cms.EDAnalyzer('Triplet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
