import FWCore.ParameterSet.Config as cms

def CSCGainsReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCGainsReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
