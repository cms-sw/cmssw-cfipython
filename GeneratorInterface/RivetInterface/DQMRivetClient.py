import FWCore.ParameterSet.Config as cms

def DQMRivetClient(**kwargs):
  mod = cms.EDAnalyzer('DQMRivetClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
