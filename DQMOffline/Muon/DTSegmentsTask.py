import FWCore.ParameterSet.Config as cms

def DTSegmentsTask(**kwargs):
  mod = cms.EDProducer('DTSegmentsTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
