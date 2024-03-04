import FWCore.ParameterSet.Config as cms

def AlcaBeamSpotFromDB(**kwargs):
  mod = cms.EDProducer('AlcaBeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
