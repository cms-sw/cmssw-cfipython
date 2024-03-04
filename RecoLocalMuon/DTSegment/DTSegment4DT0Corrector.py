import FWCore.ParameterSet.Config as cms

def DTSegment4DT0Corrector(**kwargs):
  mod = cms.EDProducer('DTSegment4DT0Corrector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
