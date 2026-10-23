import FWCore.ParameterSet.Config as cms

def DTSegment2DSLPhiQuality(*args, **kwargs):
  mod = cms.EDProducer('DTSegment2DSLPhiQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
