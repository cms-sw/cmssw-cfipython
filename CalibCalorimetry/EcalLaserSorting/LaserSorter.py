import FWCore.ParameterSet.Config as cms

def LaserSorter(**kwargs):
  mod = cms.EDAnalyzer('LaserSorter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
