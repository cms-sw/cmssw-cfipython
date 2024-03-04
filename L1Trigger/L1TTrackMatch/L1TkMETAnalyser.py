import FWCore.ParameterSet.Config as cms

def L1TkMETAnalyser(**kwargs):
  mod = cms.EDAnalyzer('L1TkMETAnalyser',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
