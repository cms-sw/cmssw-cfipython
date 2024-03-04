import FWCore.ParameterSet.Config as cms

def MuonMCClassifier(**kwargs):
  mod = cms.EDProducer('MuonMCClassifier',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
