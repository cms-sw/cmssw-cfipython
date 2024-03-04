import FWCore.ParameterSet.Config as cms

def CaloConfigWriter(**kwargs):
  mod = cms.EDAnalyzer('CaloConfigWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
