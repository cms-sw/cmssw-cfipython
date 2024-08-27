import FWCore.ParameterSet.Config as cms

def CSCCrossTalkReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCCrossTalkReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
