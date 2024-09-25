import FWCore.ParameterSet.Config as cms

def MuonSimClassifier(*args, **kwargs):
  mod = cms.EDProducer('MuonSimClassifier',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
