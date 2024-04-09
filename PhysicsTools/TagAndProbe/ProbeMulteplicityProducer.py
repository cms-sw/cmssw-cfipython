import FWCore.ParameterSet.Config as cms

def ProbeMulteplicityProducer(**kwargs):
  mod = cms.EDProducer('ProbeMulteplicityProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod