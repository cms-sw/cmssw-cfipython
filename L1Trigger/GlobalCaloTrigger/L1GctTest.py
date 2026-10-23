import FWCore.ParameterSet.Config as cms

def L1GctTest(*args, **kwargs):
  mod = cms.EDAnalyzer('L1GctTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
