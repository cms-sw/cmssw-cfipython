import FWCore.ParameterSet.Config as cms

def CSCGainsDBReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCGainsDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
