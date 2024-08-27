import FWCore.ParameterSet.Config as cms

def L1MuonRecoTreeProducer(**kwargs):
  mod = cms.EDAnalyzer('L1MuonRecoTreeProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
