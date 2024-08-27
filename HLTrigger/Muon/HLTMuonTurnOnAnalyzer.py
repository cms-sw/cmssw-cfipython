import FWCore.ParameterSet.Config as cms

def HLTMuonTurnOnAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HLTMuonTurnOnAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
