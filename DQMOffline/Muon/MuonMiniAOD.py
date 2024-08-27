import FWCore.ParameterSet.Config as cms

def MuonMiniAOD(**kwargs):
  mod = cms.EDProducer('MuonMiniAOD',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
