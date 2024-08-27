import FWCore.ParameterSet.Config as cms

def MuonRecoAnalyzer(**kwargs):
  mod = cms.EDProducer('MuonRecoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
