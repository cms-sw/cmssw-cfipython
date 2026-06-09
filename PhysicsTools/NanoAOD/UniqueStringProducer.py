import FWCore.ParameterSet.Config as cms

def UniqueStringProducer(*args, **kwargs):
  mod = cms.EDProducer('UniqueStringProducer',
    strings = cms.PSet(
      allowAnyLabel_ = cms.required.string
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
