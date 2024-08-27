import FWCore.ParameterSet.Config as cms

def MuonTimingValidator(**kwargs):
  mod = cms.EDAnalyzer('MuonTimingValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
