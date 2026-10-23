import FWCore.ParameterSet.Config as cms

def PATMuonSlimmer(*args, **kwargs):
  mod = cms.EDProducer('PATMuonSlimmer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
