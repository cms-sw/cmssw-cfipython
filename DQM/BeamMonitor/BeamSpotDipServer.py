import FWCore.ParameterSet.Config as cms

def BeamSpotDipServer(**kwargs):
  mod = cms.EDProducer('BeamSpotDipServer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
