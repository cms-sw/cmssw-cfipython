import FWCore.ParameterSet.Config as cms

def TSGFromL1Muon(*args, **kwargs):
  mod = cms.EDProducer('TSGFromL1Muon',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
