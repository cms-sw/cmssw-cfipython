import FWCore.ParameterSet.Config as cms

def MuonMETValueMapProducer(**kwargs):
  mod = cms.EDProducer('MuonMETValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
