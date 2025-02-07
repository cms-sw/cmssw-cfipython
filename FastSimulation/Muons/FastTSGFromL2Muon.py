import FWCore.ParameterSet.Config as cms

def FastTSGFromL2Muon(*args, **kwargs):
  mod = cms.EDProducer('FastTSGFromL2Muon',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
