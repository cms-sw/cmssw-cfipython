import FWCore.ParameterSet.Config as cms

def Timestamp(**kwargs):
  mod = cms.EDAnalyzer('Timestamp',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
