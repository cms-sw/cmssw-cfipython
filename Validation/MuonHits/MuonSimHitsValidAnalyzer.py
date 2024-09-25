import FWCore.ParameterSet.Config as cms

def MuonSimHitsValidAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MuonSimHitsValidAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
