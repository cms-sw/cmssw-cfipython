import FWCore.ParameterSet.Config as cms

def AlcaBeamSpotFromDB(*args, **kwargs):
  mod = cms.EDProducer('AlcaBeamSpotFromDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
