import FWCore.ParameterSet.Config as cms

def DTSegment2DSLPhiQuality(**kwargs):
  mod = cms.EDProducer('DTSegment2DSLPhiQuality',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
