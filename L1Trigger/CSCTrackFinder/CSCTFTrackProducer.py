import FWCore.ParameterSet.Config as cms

def CSCTFTrackProducer(**kwargs):
  mod = cms.EDProducer('CSCTFTrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
