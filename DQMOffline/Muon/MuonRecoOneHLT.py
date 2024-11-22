import FWCore.ParameterSet.Config as cms

def MuonRecoOneHLT(*args, **kwargs):
  mod = cms.EDProducer('MuonRecoOneHLT',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
