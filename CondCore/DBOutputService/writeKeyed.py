import FWCore.ParameterSet.Config as cms

def writeKeyed(*args, **kwargs):
  mod = cms.EDAnalyzer('writeKeyed',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
