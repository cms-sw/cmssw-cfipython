import FWCore.ParameterSet.Config as cms

def GlobalHitsProdHist(*args, **kwargs):
  mod = cms.EDProducer('GlobalHitsProdHist',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
