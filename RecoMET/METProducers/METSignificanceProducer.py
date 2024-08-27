import FWCore.ParameterSet.Config as cms

def METSignificanceProducer(**kwargs):
  mod = cms.EDProducer('METSignificanceProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
