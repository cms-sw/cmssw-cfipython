import FWCore.ParameterSet.Config as cms

def BeamHaloProducer(**kwargs):
  mod = cms.EDProducer('BeamHaloProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
