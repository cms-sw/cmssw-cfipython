import FWCore.ParameterSet.Config as cms

def DTSegment4DT0Corrector(*args, **kwargs):
  mod = cms.EDProducer('DTSegment4DT0Corrector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
