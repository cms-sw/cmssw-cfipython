import FWCore.ParameterSet.Config as cms

def CSCSegmentProducer(**kwargs):
  mod = cms.EDProducer('CSCSegmentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
