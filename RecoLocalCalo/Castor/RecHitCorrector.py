import FWCore.ParameterSet.Config as cms

def RecHitCorrector(*args, **kwargs):
  mod = cms.EDProducer('RecHitCorrector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
