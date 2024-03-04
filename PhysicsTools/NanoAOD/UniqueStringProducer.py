import FWCore.ParameterSet.Config as cms

def UniqueStringProducer(**kwargs):
  mod = cms.EDProducer('UniqueStringProducer',
    strings = cms.PSet(
      allowAnyLabel_ = cms.required.string
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
