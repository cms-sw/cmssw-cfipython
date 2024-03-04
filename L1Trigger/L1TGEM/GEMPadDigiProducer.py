import FWCore.ParameterSet.Config as cms

def GEMPadDigiProducer(**kwargs):
  mod = cms.EDProducer('GEMPadDigiProducer',
    InputCollection = cms.InputTag('simMuonGEMDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
