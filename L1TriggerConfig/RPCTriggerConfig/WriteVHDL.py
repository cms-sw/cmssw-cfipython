import FWCore.ParameterSet.Config as cms

def WriteVHDL(*args, **kwargs):
  mod = cms.EDAnalyzer('WriteVHDL',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
