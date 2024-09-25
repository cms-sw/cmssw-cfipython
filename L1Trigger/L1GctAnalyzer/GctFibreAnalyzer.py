import FWCore.ParameterSet.Config as cms

def GctFibreAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('GctFibreAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
