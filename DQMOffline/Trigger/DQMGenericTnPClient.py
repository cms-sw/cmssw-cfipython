import FWCore.ParameterSet.Config as cms

def DQMGenericTnPClient(**kwargs):
  mod = cms.EDAnalyzer('DQMGenericTnPClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
