import FWCore.ParameterSet.Config as cms

def MatacqProducer(**kwargs):
  mod = cms.EDProducer('MatacqProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
