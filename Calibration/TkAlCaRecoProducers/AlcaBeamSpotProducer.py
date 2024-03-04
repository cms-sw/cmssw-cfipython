import FWCore.ParameterSet.Config as cms

def AlcaBeamSpotProducer(**kwargs):
  mod = cms.EDProducer('AlcaBeamSpotProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
