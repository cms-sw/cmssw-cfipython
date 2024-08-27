import FWCore.ParameterSet.Config as cms

def GEMCSCLUTAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('GEMCSCLUTAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
