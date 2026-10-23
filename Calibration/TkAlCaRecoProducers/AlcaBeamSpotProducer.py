import FWCore.ParameterSet.Config as cms

def AlcaBeamSpotProducer(*args, **kwargs):
  mod = cms.EDProducer('AlcaBeamSpotProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
