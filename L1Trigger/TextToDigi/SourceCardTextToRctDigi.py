import FWCore.ParameterSet.Config as cms

def SourceCardTextToRctDigi(**kwargs):
  mod = cms.EDProducer('SourceCardTextToRctDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
