import FWCore.ParameterSet.Config as cms

def DQMOfflineHLTEventInfoClient(**kwargs):
  mod = cms.EDAnalyzer('DQMOfflineHLTEventInfoClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
