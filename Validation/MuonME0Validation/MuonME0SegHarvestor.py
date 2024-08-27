import FWCore.ParameterSet.Config as cms

def MuonME0SegHarvestor(**kwargs):
  mod = cms.EDProducer('MuonME0SegHarvestor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
