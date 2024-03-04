import FWCore.ParameterSet.Config as cms

def MuonSimClassifier(**kwargs):
  mod = cms.EDProducer('MuonSimClassifier',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
