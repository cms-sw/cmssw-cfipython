import FWCore.ParameterSet.Config as cms

def CSCDigiToPattern(**kwargs):
  mod = cms.EDAnalyzer('CSCDigiToPattern',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
