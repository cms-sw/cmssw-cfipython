import FWCore.ParameterSet.Config as cms

def CSCPedestalReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCPedestalReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
