import FWCore.ParameterSet.Config as cms

def EvtPlaneProducer(**kwargs):
  mod = cms.EDProducer('EvtPlaneProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
