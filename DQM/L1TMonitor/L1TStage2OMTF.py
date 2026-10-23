import FWCore.ParameterSet.Config as cms

def L1TStage2OMTF(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2OMTF',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
