import FWCore.ParameterSet.Config as cms

def MuonRecoTest(**kwargs):
  mod = cms.EDProducer('MuonRecoTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
