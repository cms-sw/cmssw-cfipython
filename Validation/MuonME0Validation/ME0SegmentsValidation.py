import FWCore.ParameterSet.Config as cms

def ME0SegmentsValidation(**kwargs):
  mod = cms.EDProducer('ME0SegmentsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
