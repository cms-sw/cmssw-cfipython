import FWCore.ParameterSet.Config as cms

def MuonRecoAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('MuonRecoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
