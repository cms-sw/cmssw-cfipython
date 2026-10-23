import FWCore.ParameterSet.Config as cms

def ReadMath(*args, **kwargs):
  mod = cms.EDAnalyzer('ReadMath',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
