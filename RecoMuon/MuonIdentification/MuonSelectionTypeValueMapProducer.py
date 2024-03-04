import FWCore.ParameterSet.Config as cms

def MuonSelectionTypeValueMapProducer(**kwargs):
  mod = cms.EDProducer('MuonSelectionTypeValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
