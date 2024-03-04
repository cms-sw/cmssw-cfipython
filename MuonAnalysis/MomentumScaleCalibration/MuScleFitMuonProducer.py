import FWCore.ParameterSet.Config as cms

def MuScleFitMuonProducer(**kwargs):
  mod = cms.EDProducer('MuScleFitMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
