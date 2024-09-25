import FWCore.ParameterSet.Config as cms

def MuonRecoTest(*args, **kwargs):
  mod = cms.EDProducer('MuonRecoTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
