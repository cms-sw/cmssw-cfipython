import FWCore.ParameterSet.Config as cms

def CSCDigiAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCDigiAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
