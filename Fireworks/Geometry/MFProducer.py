import FWCore.ParameterSet.Config as cms

def MFProducer(**kwargs):
  mod = cms.EDProducer('MFProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
