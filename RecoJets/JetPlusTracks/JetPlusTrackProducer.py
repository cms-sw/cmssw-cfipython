import FWCore.ParameterSet.Config as cms

def JetPlusTrackProducer(**kwargs):
  mod = cms.EDProducer('JetPlusTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
