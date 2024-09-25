import FWCore.ParameterSet.Config as cms

def MuonSelectorVertex(*args, **kwargs):
  mod = cms.EDProducer('MuonSelectorVertex',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
