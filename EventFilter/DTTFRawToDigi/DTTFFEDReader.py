import FWCore.ParameterSet.Config as cms

def DTTFFEDReader(**kwargs):
  mod = cms.EDProducer('DTTFFEDReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
