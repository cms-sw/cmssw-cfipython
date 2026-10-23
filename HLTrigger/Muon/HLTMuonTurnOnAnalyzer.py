import FWCore.ParameterSet.Config as cms

def HLTMuonTurnOnAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTMuonTurnOnAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
