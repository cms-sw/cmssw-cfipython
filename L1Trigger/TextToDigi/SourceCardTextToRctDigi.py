import FWCore.ParameterSet.Config as cms

def SourceCardTextToRctDigi(*args, **kwargs):
  mod = cms.EDProducer('SourceCardTextToRctDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
