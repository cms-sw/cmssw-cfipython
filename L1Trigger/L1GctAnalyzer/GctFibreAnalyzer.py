import FWCore.ParameterSet.Config as cms

def GctFibreAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GctFibreAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
