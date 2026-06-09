import FWCore.ParameterSet.Config as cms

def GEMPadDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('GEMPadDigiProducer',
    InputCollection = cms.InputTag('simMuonGEMDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
