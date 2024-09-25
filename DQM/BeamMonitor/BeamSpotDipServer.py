import FWCore.ParameterSet.Config as cms

def BeamSpotDipServer(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotDipServer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
