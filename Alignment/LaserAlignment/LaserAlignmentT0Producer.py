import FWCore.ParameterSet.Config as cms

def LaserAlignmentT0Producer(**kwargs):
  mod = cms.EDProducer('LaserAlignmentT0Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
