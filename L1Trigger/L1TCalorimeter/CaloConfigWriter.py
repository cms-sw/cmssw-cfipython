import FWCore.ParameterSet.Config as cms

def CaloConfigWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('CaloConfigWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
