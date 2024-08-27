import FWCore.ParameterSet.Config as cms

def CSCCrossTalkDBReadAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('CSCCrossTalkDBReadAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
