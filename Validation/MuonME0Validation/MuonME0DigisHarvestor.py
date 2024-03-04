import FWCore.ParameterSet.Config as cms

def MuonME0DigisHarvestor(**kwargs):
  mod = cms.EDProducer('MuonME0DigisHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
